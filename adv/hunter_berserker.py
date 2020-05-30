from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Hunter_Berserker

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


class Hunter_Berserker(Adv):
    comment = 'needs combo time from chain coability to keep combo & do c1 after s2'
    a1 = ('fs', 0.30)
    conf ={}
    conf['slots.a'] = The_Lurker_in_the_Woods()+Primal_Crisis()
    conf['slots.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1, fsc
        queue self.s2.check()
        `s2
        `fs3, x=1
        end
        `dodge, fsc
        `fs3
    """
    coab = ['Blade','Grace','Marth']

    def init(self):
        self.conf.fs.hit = 1
        conf_alt_fs = {
            'fs1': {
                'dmg': 296 / 100.0,
                'sp': 600,
                'charge': 24 / 60.0,
                'startup': 50 / 60.0, # 40 + 10
                'recovery': 40 / 60.0,
            },
            'fs2': {
                'dmg': 424 / 100.0,
                'sp': 960,
                'charge': 48 / 60.0,
                'startup': 50 / 60.0,
                'recovery': 40 / 60.0,
            },
            'fs3': {
                'dmg': 548 / 100.0,
                'sp': 1400,
                'charge': 72 / 60.0,
                'startup': 50 / 60.0,
                'recovery': 40 / 60.0,
            }
        }
        for n, c in conf_alt_fs.items():
            self.conf[n] = Conf(c)
            act = FS_MH(n, self.conf[n])
            self.__dict__['a_'+n] = act

        self.l_fs1 = Listener('fs1',self.l_fs1)
        self.l_fs2 = Listener('fs2',self.l_fs2)
        self.l_fs3 = Listener('fs3',self.l_fs3)
        self.fs = None

    def do_fs(self, e, name):
        log('cast','fs')
        self.__dict__['a_'+name].getdoing().cancel_by.append(name)
        self.__dict__['a_'+name].getdoing().interrupt_by.append(name)
        self.fs_before(e)
        self.update_hits('fs')
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

    def prerun(self):
        self.s1_debuff = Debuff('s1', 0.05, 10)

        self.s2_fs_boost = SingleActionBuff('s2', 0.80, 1, 'fs', 'buff', ['fs1','fs2','fs3'])

        self.a3_crit = Modifier('a3', 'crit', 'chance', 0)
        self.a3_crit.get = self.a3_crit_get
        self.a3_crit.on()

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.s1_debuff = Debuff(dst, 0.05, 10)

    def a3_crit_get(self):
        return (self.mod('def') != 1) * 0.20

    def s1_proc(self, e):
        self.s1_debuff.on()

    def s2_proc(self, e):
        self.s2_fs_boost.on(1)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)