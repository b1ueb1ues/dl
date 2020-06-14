from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Linnea

class FS_Linnea(Action):
    def __init__(self, name, conf, act=None):
        Action.__init__(self, name, conf, act)
        self.atype = 'fs'
        self.interrupt_by = ['s']
        self.cancel_by = ['s','dodge']

    def charge_speed(self):
        return self._static.c_spd_func()

    def sync_config(self, c):
        self._charge = c.charge
        self._startup = c.startup
        self._recovery = c.recovery
        self._active = c.active

    def getstartup(self):
        return (self._charge / self.charge_speed()) + (self._startup / self.speed())

class Linnea(Adv):
    a3 = ('fs',0.50)

    conf = {}
    conf['slots.a'] = The_Lurker_in_the_Woods()+Levins_Champion()
    conf['slots.d'] = Fatalis()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s2
        `s1
        `fs3
        """
    coab = ['Dagger','Grace','Axe2']

    def init(self):
        conf_alt_fs = {
            'fs1': {
                'dmg': 1551 / 100.0,
                'sp': 600,
                'charge': 30 / 60.0,
                'startup': 16 / 60.0,
                'recovery': 34 / 60.0,
                'hit': 3
            },
            'fs2': {
                'dmg': 1722 / 100.0,
                'sp': 925,
                'charge': 108 / 60.0,
                'startup': 16 / 60.0,
                'recovery': 34 / 60.0,
                'hit': 6
            },
            'fs3': {
                'dmg': 2124 / 100.0,
                'sp': 1500,
                'charge': 210 / 60.0,
                'startup': 16 / 60.0,
                'recovery': 34 / 60.0,
                'hit': 9
            }
        }
        for n, c in conf_alt_fs.items():
            self.conf[n] = Conf(c)
            act = FS_Linnea(n, self.conf[n])
            act.atype = 'fs'
            act.interrupt_by = ['s']
            act.cancel_by = ['s','dodge']
            self.__dict__['a_'+n] = act
        self.l_fs1 = Listener('fs1',self.l_fs1)
        self.l_fs2 = Listener('fs2',self.l_fs2)
        self.l_fs2 = Listener('fs3',self.l_fs3)

    def prerun(self):
        self.fs_hits = 0
        self.fs_ahits = 0
        self.fs_alt_uses = 0
        self.s2_cspd = Spdbuff(f's2_spd',0.3,15, mtype='cspd')
        self.s2_mode = 0
        self.a_s2 = self.s2.ac
        self.a_s2a = S('s2', Conf({'startup': 0.10, 'recovery': 1.3333}))

    def s1_proc(self, e):
        self.fs_alt_uses = 1

    def s2_proc(self, e):
        if self.s2_mode == 0:
            self.s2_cspd.on()
            self.s2.ac = self.a_s2a
        else:
            self.dmg_make(e.name, 14.20)
            self.hits += 3
            self.s2.ac = self.a_s2
        self.s2_mode = (self.s2_mode + 1) % 2

    def do_fs(self, e, name):
        log('cast','fs')
        e.name = name
        self.__dict__['a_'+name].getdoing().cancel_by.append(name)
        self.__dict__['a_'+name].getdoing().interrupt_by.append(name)
        self.fs_before(e)
        self.update_hits('fs')
        if name == 'fs3':
            with KillerModifier('fs_killer', 'hit', 0.2, ['poison']):
                self.dmg_make(e.name, self.conf[name+'.dmg'], 'fs')
        else:
            self.dmg_make(e.name, self.conf[name+'.dmg'], 'fs')
        self.fs_proc(e)
        self.think_pin('fs')
        self.charge(name,self.conf[name+'.sp'])

        self.fs_alt_uses = 0

    def fs_proc(self, e):
        self.update_fs_hits(self.conf[e.name+'.hit'])

    def update_fs_hits(self, fs_hits):
        self.fs_hits += fs_hits
        if self.fs_hits // 3 > self.fs_ahits:
            delta = self.fs_hits // 3 - self.fs_ahits
            self.fs_ahits = self.fs_hits // 3
            self.s1.charge(self.sp_convert(0.30*delta, self.conf.s1.sp))
        # fs always break combo
        self.hits = 0

    def l_fs1(self, e):
        self.do_fs(e, 'fs1')

    def fs1(self):
        return self.fs_alt_uses and self.a_fs1()

    def l_fs2(self, e):
        self.do_fs(e, 'fs2')

    def fs2(self):
        return self.fs_alt_uses and self.a_fs2()

    def l_fs3(self, e):
        self.do_fs(e, 'fs3')

    def fs3(self):
        return self.fs_alt_uses and self.a_fs3()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)