from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Zhu_Bajie

class FS_MH(Action):
    def __init__(self, name, conf, act=None):
        Action.__init__(self, name, conf, act)
        self.atype = 'fs'
        self.interrupt_by = ['s']
        self.cancel_by = ['s','dodge']

    def act(self, action):
        self.act_event.name = 'fs'
        self.act_event.idx = self.idx
        self.act_event()

    def sync_config(self, c):
        self._charge = c.charge
        self._startup = c.startup
        self._recovery = c.recovery
        self._active = c.active

    def getstartup(self):
        return self._charge + (self._startup / self.speed())

class Zhu_Bajie(Adv):
    a3 = ('ro', 0.10)

    conf = {}
    conf['slots.a'] = Mega_Friends()+Dear_Diary()
    conf['slots.d'] = Cupid()
    conf['slots.paralysis.d'] = Corsaint_Phoenix()
    conf['acl'] = """
        `s2, fsc
        `s1, fsc
        `dodge, fsc
        `fs3
        """
    coab = ['Blade','Grace','Peony']

    def prerun(self):
        self.conf.fs.hit = 1
        conf_alt_fs = {
            'fs1': {
                'dmg': 207 / 100.0,
                'sp': 600,
                'charge': 24 / 60.0,
                'startup': 20 / 60.0,
                'recovery': 20 / 60.0,
            },
            'fs2': {
                'dmg': 297 / 100.0,
                'sp': 960,
                'charge': 48 / 60.0,
                'startup': 20 / 60.0,
                'recovery': 20 / 60.0,
            },
            'fs3': {
                'dmg': 383 / 100.0,
                'sp': 1400,
                'charge': 72 / 60.0,
                'startup': 20 / 60.0,
                'recovery': 20 / 60.0,
            }
        }
        for n, c in conf_alt_fs.items():
            self.conf[n] = Conf(c)
            act = FS_MH(n, self.conf[n])
            self.__dict__['a_'+n] = act

        self.l_fs1 = Listener('fs1',self.l_fs1)
        self.l_fs2 = Listener('fs2',self.l_fs2)
        self.l_fs3 = Listener('fs3',self.l_fs3)

    def do_fs(self, e, name):
        log('cast','fs')
        self.__dict__['a_'+name].getdoing().cancel_by.append(name)
        self.__dict__['a_'+name].getdoing().interrupt_by.append(name)
        self.fs_before(e)
        self.update_hits('fs')
        with KillerModifier(e.name, 'hit', 0.5, ['paralysis']):
            self.dmg_make('fs', self.conf[name+'.dmg'], 'fs')
        self.fs_proc(e)
        self.think_pin('fs')
        self.charge(name,self.conf[name+'.sp'])

    def l_fs1(self, e):
        self.do_fs(e, 'fs1')

    def fs1(self):
        return self.a_fs1()

    def l_fs2(self, e):
        self.do_fs(e, 'fs2')

    def fs2(self):
        return self.a_fs2()

    def l_fs3(self, e):
        self.do_fs(e, 'fs3')

    def fs3(self):
        return self.a_fs3()

    def s1_proc(self, e):
        with CrisisModifier(e.name, 1.15, self.hp):
            self.dmg_make(e.name, 8.52)
        self.afflics.stun(e.name, 110)

    def s2_proc(self, e):
        if self.hp > 30:
            self.set_hp(20)
        else:
            Selfbuff(e.name, 0.15, 10).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)