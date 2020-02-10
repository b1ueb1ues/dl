from core.advbase import Action
from core.timeline import Event, Timer, now
from core.log import log

class DragonForm(Action):
    def __init__(self, name, conf, adv, ds_proc=None, timing=None):
        self.name = name
        self.conf = conf
        self.adv = adv
        
        self.ds_proc = ds_proc if ds_proc is not None else self.default_ds_proc
        self.has_skill = True
        self.act_list = []

        self.action_timer = None

        shift_time = self.conf.dshift.startup + self.conf.duration
        self.shift_start_time = 0
        self.shift_damage_sum = 0
        self.shift_end_timer = Timer(self.d_shift_end, timeout=shift_time)
        self.idle_event = Event('idle')

        self.c_act_name = None
        self.c_act_conf = None
        self.dracolith_mod = self.adv.Modifier('dracolith', 'att', 'hit', self.conf.dracolith)
        self.dracolith_mod.off()

        self.dragon_gauge = 0
        if timing is None:
            from adv.adv_test import sim_duration
            timing = int(sim_duration/10)
        self.dragon_gauge_timer = Timer(self.auto_gauge, repeat=1).on(timing)

    def default_ds_proc(self):
        try:
            return self.adv.dmg_make('o_d_ds',self.conf.ds.dmg,'s')
        except:
            return 0

    def auto_gauge(self, t):
        self.charge_gauge(10)

    def charge_gauge(self, value):
        if self.status != -1:
            if self.adv.slots.c.wt == 'sword':
                self.dragon_gauge += value*1.15
            else:
                self.dragon_gauge += value
            self.dragon_gauge = min(self.dragon_gauge, 100)
            log('dragon', 'gauge', '{:.2f} / 100'.format(self.dragon_gauge))

    def d_shift_end(self, t):
        duration = now()-self.shift_start_time
        log('dragon_end', self.name, 
            '{:.2f} dmg over {:.2f}s'.format(self.shift_damage_sum, duration),
            '{:.2f} dps'.format(self.shift_damage_sum/duration))
        if self.action_timer is not None:
            self.action_timer.off()
            self.action_timer = None
        self.dracolith_mod.off()
        self.has_skill = True
        self.status = -2
        self._setprev() # turn self from doing to prev
        self._static.doing = self.nop
        self.idle_event()

    def act_timer(self, act, time):
        self.action_timer = Timer(act, time / self.speed())
        return self.action_timer.on()

    def d_act_start(self, name):
        if name in self.conf and self._static.doing == self and self.action_timer is None:
            prev_act = self.c_act_name
            prev_conf = self.c_act_conf
            self.c_act_name = name
            self.c_act_conf = self.conf[name]
            if self.c_act_name == 'ds' and prev_act is not None:
                self.act_timer(self.d_act_do, self.c_act_conf.startup-prev_conf.recovery)
            else:
                self.act_timer(self.d_act_do, self.c_act_conf.startup)

    def d_act_do(self, t):
        if self.c_act_name == 'ds':
            self.has_skill = False
            self.shift_end_timer.timing += self.conf.ds.startup
            self.shift_damage_sum += self.ds_proc()
        elif self.c_act_name == 'end':
            self.shift_end_timer.off()
            self.d_shift_end(None)
            return
        else:
            # dname = self.c_act_name[:-1] if self.c_act_name != 'dshift' else self.c_act_name
            self.shift_damage_sum += self.adv.dmg_make('o_d_'+self.c_act_name, self.c_act_conf.dmg)
        if self.c_act_conf.hit > -1:
            self.adv.hits += self.c_act_conf.hit
        else:
            self.adv.hits = -self.c_act_conf.hit
        self.act_timer(self.d_act_next, self.c_act_conf.recovery)

    def d_act_next(self, t):
        self.action_timer = None
        if len(self.act_list) > 0:
            nact = self.act_list.pop(0)
            self.d_act_start(nact)
        elif self.c_act_name[0:2] == 'dx':
            nx = 'dx{}'.format(int(self.c_act_name[2])+1)
            if nx in self.conf:
                self.d_act_start(nx)
            else:
                if self.has_skill:
                    self.d_act_start('ds')
                else:
                    self.d_act_start('dx1')
        else:
            self.d_act_start('dx1')

    def parse_act(self):
        if 'act' in self.conf:
            self.act_list = []
            for a in self.conf.act.split(' '):
                if a[0] == 'c' or a[0] == 'x':
                    for i in range(1, int(a[1])+1):
                        dxseq = 'dx{}'.format(i)
                        if dxseq in self.conf:
                            self.act_list.append(dxseq)
                elif a == 's' or a == 'ds':
                    self.act_list.append('ds')
                elif a == 'end':
                    self.act_list.append('end')

    def __call__(self):
        if self.dragon_gauge >= 50:
            log('dragon_start', self.name)
            self.parse_act()
            self.dragon_gauge -= 50
            self.has_skill = True
            self.status = -1
            self._setdoing()
            self.shift_start_time = now()
            self.shift_end_timer.on()
            self.dracolith_mod.on()
            # self.adv.shift_proc() for weird interactions
            Event('dragon')()
            self.d_act_start('dshift')
            return True
        else:
            return False