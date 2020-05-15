from core.advbase import Action, S
from core.timeline import Event, Timer, now
from core.log import log
from math import ceil

class DragonForm(Action):
    def __init__(self, name, conf, adv, ds_proc):
        self.name = name
        self.conf = conf
        self.adv = adv
        self.cancel_by = []
        self.interrupt_by = []
        self.disabled = False
        self.shift_event = Event('dragon')
        self.end_event = Event('dragon_end')

        self.ds_proc = ds_proc
        self.ds_reset()
        self.act_list = []
        self.act_sum = []

        self.dx_list = ['dx{}'.format(i) for i in range(1, 6) if 'dmg' in self.conf['dx{}'.format(i)]]

        self.ds_event = Event('s')
        self.ds_event.name = 'ds'

        self.action_timer = None

        self.shift_start_time = 0
        self.shift_damage_sum = 0
        self.shift_end_timer = Timer(self.d_shift_end)
        self.idle_event = Event('idle')

        self.c_act_name = None
        self.c_act_conf = None
        self.dracolith_mod = self.adv.Modifier('dracolith', 'att', 'dragon', 0)
        self.dracolith_mod.off()
        self.off_ele_mod = None
        if self.adv.slots.c.ele != self.adv.slots.d.ele:
            self.off_ele_mod = self.adv.Modifier('off_ele', 'att', 'dragon', -1/3)
            self.off_ele_mod.off()

        self.dragon_gauge = 0
        self.dragon_gauge_val = self.conf.gauge_val
        self.dragon_gauge_timer = Timer(self.auto_gauge, timeout=max(1, self.conf.gauge_iv), repeat=1).on()
        self.dragon_gauge_timer_diff = 0
        self.max_gauge = 1000
        self.shift_cost = 500

        self.shift_count = 0
        self.shift_silence = False

        self.is_dragondrive = False

    def set_dragondrive(self, dd_buff, max_gauge=3000, shift_cost=1200, drain=150):
        self.disabled = False
        self.is_dragondrive = True
        self.shift_event = Event('dragondrive')
        self.dragondrive_end_event = Event('dragondrive_end')
        ratio = max_gauge / self.max_gauge
        self.dragon_gauge *= ratio
        self.dragon_gauge_val *= ratio
        self.max_gauge = max_gauge
        self.shift_cost = shift_cost # does not deduct, but need to have this much pt to shift
        self.drain = drain
        self.dragondrive_buff = dd_buff
        self.dragondrive_timer = Timer(self.d_dragondrive_end)
        return self.dragondrive_buff

    def end_silence(self, t):
        self.shift_silence = False

    def dodge_cancel(self):
        if len(self.dx_list) <= 0:
            return False
        combo = self.conf[self.dx_list[-1]].recovery / self.speed()
        dodge = self.conf.dodge.startup
        return combo > dodge

    def auto_gauge(self, t):
        self.charge_gauge(self.dragon_gauge_val)

    def pause_auto_gauge(self):
        self.dragon_gauge_timer_diff = self.dragon_gauge_timer.timing - now()
        self.dragon_gauge_timer.off()

    def resume_auto_gauge(self, t):
        self.auto_gauge(t)
        self.dragon_gauge_timer.on()

    def add_drive_gauge_time(self, delta, skill_pause=False):
        max_duration = self.max_gauge/self.drain
        duration = self.dragondrive_timer.timing - now()
        max_add = max_duration - duration
        if skill_pause:
            add_time = min(delta, max_add)
        else:
            add_time = min(delta/self.drain, max_add)
        self.dragondrive_timer.add(add_time)
        duration = self.dragondrive_timer.timing - now()
        if duration <= 0:
            self.d_dragondrive_end('<gauge deplete>')
        else:
            self.dragon_gauge = (duration/max_duration)*self.max_gauge
            if add_time > 0:
                log('drive_time' if not skill_pause else 'skill_pause', f'{add_time:+2.4}', f'{duration:2.4}', f'{int(self.dragon_gauge)}/{int(self.max_gauge)}')

    def charge_gauge(self, value, utp=False, dhaste=None):
        if dhaste is None:
            dhaste = not utp
        dh = self.adv.mod('dh') if dhaste else 1
        if not utp:
            value *= 10
        value = self.adv.sp_convert(dh, value)
        delta = min(self.dragon_gauge+value, self.max_gauge) - self.dragon_gauge
        if self.is_dragondrive and self.dragondrive_buff.get():
            self.add_drive_gauge_time(delta)
        elif delta > 0:
            self.dragon_gauge += delta
            if utp:
                log('dragon_gauge', '{:+} utp'.format(int(delta)), f'{int(self.dragon_gauge)}/{int(self.max_gauge)}')
            else:
                log('dragon_gauge', '{:+.2f}%'.format(delta/self.max_gauge*100), '{:.2f}%'.format(self.dragon_gauge/self.max_gauge*100))

    def dtime(self):
        return self.conf.dshift.startup + self.conf.duration * self.adv.mod('dt') + self.conf.exhilaration * (self.off_ele_mod is None)

    def ddamage(self):
        return self.conf.dracolith + self.adv.mod('da') - 1

    def ds_check(self):
        return self.skill_use > 0 and self.skill_spc >= self.skill_sp

    def ds_reset(self):
        self.skill_use = self.conf.skill_use
        self.skill_sp = 0 if self.conf.skill_use == 1 else 30
        self.skill_spc = self.skill_sp

    def d_shift_end(self, t):
        if self.action_timer is not None:
            self.action_timer.off()
            self.action_timer = None
        duration = now()-self.shift_start_time
        log(self.name, '{:.2f}dmg / {:.2f}s, {:.2f} dps'.format(self.shift_damage_sum, duration, self.shift_damage_sum/duration), ' '.join(self.act_sum))
        self.act_sum = []
        self.act_list = []
        self.dracolith_mod.off()
        if self.off_ele_mod is not None:
            self.off_ele_mod.off()
        self.ds_reset()
        if not self.is_dragondrive:
            self.shift_silence = True
            Timer(self.end_silence).on(10)
            Timer(self.resume_auto_gauge).on(self.dragon_gauge_timer_diff)
        self.status = -2
        self._setprev() # turn self from doing to prev
        self._static.doing = self.nop
        self.end_event()
        self.idle_event()

    def d_dragondrive_end(self, t):
        self.dragon_gauge = 0
        log('dragondrive', 'end', t if isinstance(t, str) else '<timeout>')
        self.dragondrive_buff.off()
        self.shift_silence = True
        Timer(self.end_silence).on(10)
        self.status = -2
        self._setprev() # turn self from doing to prev
        self._static.doing = self.nop
        self.dragondrive_end_event()
        self.idle_event()

    def act_timer(self, act, time, next_action=None):
        if self.c_act_name == 'dodge':
            self.action_timer = Timer(act, time)
        else:
            self.action_timer = Timer(act, time / self.speed())
        self.action_timer.next_action = next_action
        return self.action_timer.on()

    def d_act_start_t(self, t):
        self.action_timer = None
        self.d_act_start(t.next_action)

    def d_act_start(self, name):
        if name in self.conf and self._static.doing == self and self.action_timer is None:
            self.prev_act = self.c_act_name
            self.prev_conf = self.c_act_conf
            self.c_act_name = name
            self.c_act_conf = self.conf[name]
            self.act_timer(self.d_act_do, self.c_act_conf.startup)

    def d_act_do(self, t):
        if self.c_act_name == 'ds':
            self.skill_use -= 1
            self.skill_spc = 0
            self.ds_event()
            self.shift_damage_sum += self.ds_proc() or 0
            self.shift_end_timer.add(self.conf.ds.startup+self.conf.ds.recovery)
            self.act_sum.append('s')
        elif self.c_act_name == 'end':
            self.d_shift_end(None)
            self.shift_end_timer.off()
            return
        elif self.c_act_name != 'dodge':
            # dname = self.c_act_name[:-1] if self.c_act_name != 'dshift' else self.c_act_name
            self.shift_damage_sum += self.adv.dmg_make(self.c_act_name, self.c_act_conf.dmg, 'x' if self.c_act_name != 'dshift' else self.c_act_name)
            if self.c_act_name.startswith('dx'):
                if len(self.act_sum) > 0 and self.act_sum[-1][0] == 'c' and int(self.act_sum[-1][1]) < int(self.c_act_name[-1]):
                    self.act_sum[-1] = 'c'+self.c_act_name[-1]
                else:
                    self.act_sum.append('c'+self.c_act_name[-1])
                if self.skill_sp > 0 and self.skill_spc < self.skill_sp:
                    self.skill_spc += self.adv.sp_convert(self.adv.sp_mod('x'), 5)
                    if self.skill_spc > self.skill_sp:
                        self.skill_spc = self.skill_sp
                    log(self.c_act_name, 'sp', f'{self.skill_spc}/{self.skill_sp}')
        if self.c_act_conf.hit > -1:
            self.adv.hits += self.c_act_conf.hit
        else:
            self.adv.hits = -self.c_act_conf.hit
        self.d_act_next()

    def d_act_next(self):
        nact = None
        if len(self.act_list) > 0:
            if self.act_list[0] != 'ds' or self.ds_check():
                nact = self.act_list.pop(0)
        if nact is None:
            if self.c_act_name[0:2] == 'dx':
                nact = 'dx{}'.format(int(self.c_act_name[2])+1)
                if not nact in self.dx_list:
                    if self.ds_check():
                        nact = 'ds'
                    elif self.dodge_cancel():
                        nact = 'dodge'
                    else:
                        nact = 'dx1'
            else:
                nact = 'dx1'
        if nact == 'ds' or nact == 'dodge' or (nact == 'end' and self.c_act_name != 'ds'): # cancel
            self.act_timer(self.d_act_start_t, self.conf.latency, nact)
        else: # regular recovery
            self.act_timer(self.d_act_start_t, self.c_act_conf.recovery, nact)

    def parse_act(self, act_str):
        act_str = act_str.strip()
        self.act_list = []
        skill_usage = 0

        for a in act_str.split(' '):
            if a[0] == 'c' or a[0] == 'x':
                for i in range(1, int(a[1])+1):
                    dxseq = 'dx{}'.format(i)
                    if dxseq in self.dx_list:
                        self.act_list.append(dxseq)
                if self.dodge_cancel() or self.act_list[-1] != self.dx_list[-1]:
                    self.act_list.append('dodge')
            else:
                if len(self.act_list) > 0 and self.act_list[-1] == 'dodge':
                    self.act_list.pop()
                if (a == 's' or a == 'ds') and skill_usage < self.skill_use:
                    self.act_list.append('ds')
                    skill_usage += 1
                elif a == 'end':
                    self.act_list.append('end')
                elif a == 'dodge':
                    self.act_list.append('dodge')

    def act(self, act_str):
        self.parse_act(act_str)
        return self()

    def check(self, dryrun=True):
        if self.disabled or self.shift_silence:
            return False
        if self.dragon_gauge < self.shift_cost and not (self.is_dragondrive and self.dragondrive_buff.get()):
            return False
        doing = self.getdoing()
        if not doing.idle:
            if isinstance(doing, S) or isinstance(doing, DragonForm):
                return False
            if not dryrun:
                if doing.status == -1:
                    doing.startup_timer.off()
                    log('interrupt', doing.name , 'by '+self.name, 'after {:.2f}s'.format(now()-doing.startup_start))
                elif doing.status == 1:
                    doing.recovery_timer.off()
                    log('cancel', doing.name , 'by '+self.name, 'after {:.2f}s'.format(now()-doing.recover_start))
        return True

    def __call__(self):
        if not self.check(dryrun=False):
            return False
        if self.is_dragondrive:
            self.act_list = ['end']
            if self.dragondrive_buff.get():
                self.d_dragondrive_end('<turn off>')
                return True
            else:
                log('cast', 'dragondrive', self.name, f'base duration {self.dragon_gauge/self.drain:.4}s')
                self.dragondrive_timer.on(self.dragon_gauge/self.drain)
                self.dragondrive_buff.on()
        else:
            log('cast', 'dshift', self.name)
            if len(self.act_list) == 0:
                self.parse_act(self.conf.act)
            self.dragon_gauge -= self.shift_cost
            self.dracolith_mod.mod_value = self.ddamage()
            self.dracolith_mod.on()
            if self.off_ele_mod is not None:
                self.off_ele_mod.on()
            self.pause_auto_gauge()
        self.shift_count += 1
        self.shift_damage_sum = 0
        self.status = -1
        self._setdoing()
        self.shift_start_time = now()
        self.shift_end_timer.on(self.dtime())
        self.shift_event()
        self.d_act_start('dshift')
        return True
