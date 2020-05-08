from core.advbase import Fs_group, Fs, X, Event
from core.timeline import Listener, Timer
from core.log import log
from core.config import Conf
from core.dragonform import DragonForm

class Fs_alt:
    def __init__(self, adv, conf, fs_proc=None):
        self.adv = adv
        self.a_fs_og = adv.a_fs
        self.conf_og = adv.conf
        self.fs_proc_og = adv.fs_proc
        self.conf_alt = adv.conf + Conf(conf)
        self.a_fs_alt = Fs_group('fs_alt', self.conf_alt)
        self.fs_proc_alt = fs_proc
        self.uses = 0
        self.has_fsf = False
        if 'fsf' in conf:
            self.a_fsf_og = adv.a_fsf
            self.a_fsf_alt = Fs('fsf', conf.fsf)
            self.a_fsf_alt.act_event = Event('none')
            self.has_fsf = True

    def fs_proc(self, e):
        if callable(self.fs_proc_alt):
            self.fs_proc_alt(e)
        if self.uses != -1:
            self.uses -= 1
            if self.uses == 0:
                self.off()

    def on(self, uses = 1):
        log('debug', 'fs_alt on', uses)
        self.uses = uses
        self.adv.a_fs = self.a_fs_alt
        self.adv.conf = self.conf_alt
        self.adv.fs_proc = self.fs_proc
        if self.has_fsf:
            self.adv.fsf = self.a_fsf_alt

    def off(self):
        log('debug', 'fs_alt off', 0)
        self.uses = 0
        self.adv.a_fs = self.a_fs_og
        self.adv.conf = self.conf_og
        self.adv.fs_proc = self.fs_proc_og
        if self.has_fsf:
            self.adv.fsf = self.a_fsf_og

    def get(self):
        return self.uses != 0

class X_alt:
    def __init__(self, adv, name, conf, x_proc=None, no_fs=False, no_dodge=False):
        self.conf = Conf(conf)
        self.adv = adv
        self.name = name
        self.x_og = adv.x
        self.a_x_alt = {}
        if x_proc:
            self.x_proc = x_proc
            self.l_x_alt = Listener('x', self.l_x).off()
        else:
            self.l_x_alt = None
        self.no_fs = no_fs
        self.no_dodge = no_dodge
        self.fs_og = adv.fs
        self.dodge_og = adv.dodge
        self.xmax = 1
        n = 'x{}'.format(self.xmax)
        while n in self.conf:
            self.a_x_alt[self.xmax] = X((n, self.xmax), self.conf[n])
            self.xmax += 1
            n = 'x{}'.format(self.xmax)
        self.xmax -= 1
        self.active = False
        self.xstart = None
        self.zeroed = None

    def x_alt(self):
        x_prev = self.adv.action.getprev()
        if x_prev in self.a_x_alt.values() and x_prev.index < self.xmax:
            x_seq = x_prev.index+1
        else:
            x_seq = 1
        return self.a_x_alt[x_seq]()

    def l_x(self, e):
        self.x_proc(e)
        self.adv.think_pin('x')

    def act_off(self):
        return False
    
    def on(self):
        if not self.active:
            if self.zeroed is not None:
                self.zeroed[0].index = self.zeroed[1]
                self.zeroed = None

            act = self.a_x_alt[1]
            doing = act._static.doing
            if not doing.idle and doing.status == -1:
                try:
                    doing.startup_timer.off()
                    doing._setprev()
                    doing._static.doing = doing.nop
                    act()
                except:
                    pass

            log('debug', '{} x_alt on'.format(self.name))
            self.active = True
            self.adv.x = self.x_alt
            if self.l_x_alt:
                self.adv.l_x.off()
                self.l_x_alt.on()
            if self.no_fs:
                self.adv.fs = self.act_off
            if self.no_dodge:
                self.adv.dodge = self.act_off
                
    def off(self):
        if self.active:
            log('debug', '{} x_alt off'.format(self.name))
            self.active = False
            self.adv.x = self.x_og
            if self.l_x_alt:
                self.l_x_alt.off()
                self.adv.l_x.on()
            if self.no_fs:
                self.adv.fs = self.fs_og
            if self.no_dodge:
                self.adv.dodge = self.dodge_og

            doing = self.a_x_alt[1]._static.doing
            self.zeroed = (doing, doing.index)
            doing.index = 0