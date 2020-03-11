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

        self.ds_proc = ds_proc
        self.skill_use = self.conf.skill_use
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
        self.dragon_gauge_timer = Timer(self.auto_gauge, repeat=1).on(max(1, self.conf.gauge_iv))

        self.shift_count = 0

    def dodge_cancel(self):
        if len(self.dx_list) <= 0:
            return False
        combo = self.conf[self.dx_list[-1]].recovery / self.speed()
        dodge = self.conf.dodge.startup
        return combo > dodge

    def auto_gauge(self, t):
        self.charge_gauge(self.conf.gauge_val)

    def charge_gauge(self, value):
        # if self.status != -1:
        # ignore dragonform blocking gauge (as it would in game) to avoid break-pointy bullshit
        value = ceil(value*self.adv.mod('dh')*10)/10
        self.dragon_gauge += value
        self.dragon_gauge = min(self.dragon_gauge, 100)
        log('dragon_gauge', '+{:.2f}%'.format(value), '{:.2f}%'.format(self.dragon_gauge))

    def dtime(self):
        return self.conf.dshift.startup + self.conf.duration * self.adv.mod('dt') + self.conf.exhilaration * (self.off_ele_mod is None)

    def ddamage(self):
        return self.conf.dracolith + self.adv.mod('da') - 1

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
            self.off_ele_mod.on()
        self.skill_use = self.conf.skill_use
        self.status = -2
        self._setprev() # turn self from doing to prev
        self._static.doing = self.nop
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
            self.ds_event()
            self.shift_damage_sum += self.ds_proc()
            self.shift_end_timer.add(self.conf.ds.startup+self.conf.ds.recovery)
            self.act_sum.append('s')
        elif self.c_act_name == 'end':
            self.d_shift_end(None)
            self.shift_end_timer.off()
            return
        elif self.c_act_name != 'dodge':
            # dname = self.c_act_name[:-1] if self.c_act_name != 'dshift' else self.c_act_name
            self.shift_damage_sum += self.adv.dmg_make(self.c_act_name, self.c_act_conf.dmg)
            if self.c_act_name.startswith('dx'):
                if len(self.act_sum) > 0 and self.act_sum[-1][0] == 'c' and int(self.act_sum[-1][1]) < int(self.c_act_name[-1]):
                    self.act_sum[-1] = 'c'+self.c_act_name[-1]
                else:
                    self.act_sum.append('c'+self.c_act_name[-1])
        if self.c_act_conf.hit > -1:
            self.adv.hits += self.c_act_conf.hit
        else:
            self.adv.hits = -self.c_act_conf.hit
        self.d_act_next()

    def d_act_next(self):
        if len(self.act_list) > 0:
            nact = self.act_list.pop(0)
        else:
            if self.c_act_name[0:2] == 'dx':
                nact = 'dx{}'.format(int(self.c_act_name[2])+1)
                if not nact in self.dx_list:
                    if self.skill_use > 0:
                        nact = 'ds'
                    elif self.dodge_cancel():
                        nact = 'dodge'
                    else:
                        nact = 'dx1'
            else:
                nact = 'dx1'
        if nact == 'ds' or nact == 'dodge': # cancel
            self.act_timer(self.d_act_start_t, self.conf.latency, nact)
        else: # regular recovery
            self.act_timer(self.d_act_start_t, self.c_act_conf.recovery, nact)

    def parse_act(self, act_str):
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

    def __call__(self):
        if self.disabled:
            return False
        if self.dragon_gauge < 50:
            return False
        doing = self.getdoing()
        if not doing.idle:
            if isinstance(doing, S) or isinstance(doing, DragonForm):
                return False
            if doing.status == -1:
                doing.startup_timer.off()
                log('interrupt', doing.name , 'by '+self.name, 'after {:.2f}s'.format(now()-doing.startup_start))
            elif doing.status == 1:
                doing.recovery_timer.off()
                log('cancel', doing.name , 'by '+self.name, 'after {:.2f}s'.format(now()-doing.recover_start))
        log('dragon_start', self.name)
        self.shift_count += 1
        if len(self.act_list) == 0:
            self.parse_act(self.conf.act)
        self.shift_damage_sum = 0
        self.dragon_gauge -= 50
        self.status = -1
        self._setdoing()
        self.shift_start_time = now()
        self.shift_end_timer.on(self.dtime())
        self.dracolith_mod.mod_value = self.ddamage()
        self.dracolith_mod.on()
        if self.off_ele_mod is not None:
            self.off_ele_mod.on()
        Event('dragon')()
        log('cast', 'dshift')
        self.d_act_start('dshift')
        return True