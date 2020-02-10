from core.advbase import Action, S
from core.timeline import Event, Timer, now
from core.log import log

class DragonForm(Action):
    def __init__(self, name, conf, adv, ds_proc, timing=None):
        self.name = name
        self.conf = conf
        self.adv = adv
        self.cancel_by = []
        self.interrupt_by = []

        self.ds_proc = ds_proc
        self.has_skill = True
        self.act_list = []
        self.dx_last = ['dx{}'.format(i) for i in range(1, 6) if 'dx{}'.format(i) in self.conf][-1]

        self.action_timer = None

        self.shift_start_time = 0
        self.shift_damage_sum = 0
        self.shift_end_timer = Timer(self.d_shift_end)
        self.idle_event = Event('idle')

        self.c_act_name = None
        self.c_act_conf = None
        self.dracolith_mod = self.adv.Modifier('dracolith', 'att', 'dragon', 0)
        self.dracolith_mod.off()

        self.dragon_gauge = 0
        if timing is None:
            from adv.adv_test import sim_duration
            timing = int(sim_duration/10)
        self.dragon_gauge_timer = Timer(self.auto_gauge, repeat=1).on(timing)

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
        if self.action_timer is not None:
            self.action_timer.off()
            self.action_timer = None
        duration = now()-self.shift_start_time
        log('dragon_end', self.name, 
            '{:.2f} dmg / {:.2f}s'.format(self.shift_damage_sum, duration),
            '{:.2f} dps'.format(self.shift_damage_sum/duration))
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
            self.prev_act = self.c_act_name
            self.prev_conf = self.c_act_conf
            self.c_act_name = name
            self.c_act_conf = self.conf[name]
            self.act_timer(self.d_act_do, self.c_act_conf.startup)

    def d_act_do(self, t):
        if self.c_act_name == 'ds':
            self.has_skill = False
            self.shift_end_timer.timing += self.conf.ds.startup+self.conf.ds.recovery
            self.shift_damage_sum += self.ds_proc()
        elif self.c_act_name == 'end':
            self.d_shift_end(None)
            self.shift_end_timer.off()
            return
        else:
            # dname = self.c_act_name[:-1] if self.c_act_name != 'dshift' else self.c_act_name
            self.shift_damage_sum += self.adv.dmg_make('d_'+self.c_act_name, self.c_act_conf.dmg)
            if self.dx_last == self.c_act_name:
                log('dx', self.c_act_name, 0, '-------------------------------------c'+self.dx_last[-1])
        if self.c_act_conf.hit > -1:
            self.adv.hits += self.c_act_conf.hit
        else:
            self.adv.hits = -self.c_act_conf.hit
        if self.c_act_name == 'ds' and self.prev_act is not None:
            self.act_timer(self.d_act_next, max(0, self.c_act_conf.recovery-self.prev_conf.recovery))
        else:
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
        doing = self.getdoing()
        if isinstance(doing, S):
            if not doing.idle:
                return False
        if self.dragon_gauge >= 50:
            log('dragon_start', self.name)
            self.parse_act()
            self.dragon_gauge -= 50
            self.has_skill = True
            self.status = -1
            self._setdoing()
            # I hope there are never dragon damage or dragon time buff skills ever :bolbjed:
            self.shift_start_time = now()
            self.shift_end_timer.on(self.conf.dshift.startup + self.conf.duration * self.conf.dragon_time)
            self.dracolith_mod.mod_value = self.conf.dracolith
            self.dracolith_mod.on()
            Event('dragon')()
            self.d_act_start('dshift')
            return True
        else:
            return False