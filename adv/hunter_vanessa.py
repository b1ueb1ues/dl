from core.advbase import *
from slot.a import *

def module():
    return Hunter_Vanessa

class FS_MH(Action):
    def __init__(self, name, conf, act=None):
        Action.__init__(self, name, conf, act)
        self.atype = 'fs'
        self.interrupt_by = ['s']
        self.cancel_by = ['s','dodge']

    def sync_config(self, c):
        self._charge = c.charge
        self._startup = c.startup
        self._recovery = c.recovery
        self._active = c.active

    def getstartup(self):
        return self._charge + (self._startup / self.speed())

class Hunter_Vanessa(Adv):
    a1 = ('fs', 0.30)

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon, fsc
        `fs2, s1.charged>=s1.sp-self.sp_val('fs2')
        `s1, x=5 or fsc
        `s2, not self.s2_att_boost.get()
        `s3, x=5 or fsc
    """
    coab = ['Sharena','Dagger','Peony']
    conf['afflict_res.paralysis'] = 0

    def d_slots(self):
        if self.duration <= 90:
            self.slots.a = Resounding_Rendition()+The_Chocolatiers()

    def init(self):
        self.conf.fs.hit = 1
        conf_alt_fs = {
            'fs1': {
                'dmg': 143 / 100.0,
                'sp': 100,
                'charge': 24 / 60.0,
                'startup': 17 / 60.0,
                'recovery': 46 / 60.0
            },
            'fs2': {
                'dmg': 370 / 100.0,
                'sp': 300,
                'charge': 72 / 60.0,
                'startup': 17 / 60.0,
                'recovery': 46 / 60.0
            }
        }
        for n, c in conf_alt_fs.items():
            self.conf[n] = Conf(c)
            act = FS_MH(n, self.conf[n])
            act.atype = 'fs'
            act.interrupt_by = ['s']
            act.cancel_by = ['s','dodge']
            self.__dict__['a_'+n] = act
        
        self.l_fs1 = Listener('fs1',self.l_fs1)
        self.l_fs2 = Listener('fs2',self.l_fs2)
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

    def prerun(self):
        self.s2_att_boost = Selfbuff('s2', 0.30, 90, 'att', 'buff')

        self.a3_crit = Modifier('a3', 'crit', 'chance', 0)
        self.a3_crit.get = self.a3_crit_get
        self.a3_crit.on()

        self.fs_debuff = Debuff('fs',0.05,15)

    def a3_crit_get(self):
        return (self.mod('def') != 1) * 0.20

    def s1_proc(self, e):
        self.afflics.paralysis(e.name,120, 0.97)

    def s2_proc(self, e):
        self.s2_att_boost.on()

    def fs_proc(self, e):
        if e.name == 'fs2':
            self.fs_debuff.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)