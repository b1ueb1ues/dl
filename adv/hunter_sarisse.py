from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Hunter_Sarisse

class FS_Speedable(Action):
    def __init__(self, name=None, conf=None, act=None):
        super().__init__(name, conf, act)
        self.atype = 'fs'
        self.interrupt_by = ['s']
        self.cancel_by = ['s','dodge']
        self.fs_speed = 1.2
        self.t_fs_speed = Timer(self.fs_speed_off)
        self.l_fs_speed= Listener('fs_speed_buff', self.fs_speed_on)
        self._startup_a = 0

    def act(self, action):
        self.act_event.name = 'fs'
        self.act_event.idx = self.idx
        self.act_event()

    def fs_speed_on(self, e):
        self.fs_speed = 1.5
        self.t_fs_speed = self.t_fs_speed.on(30)

    def fs_speed_off(self, t):
        self.fs_speed = 1.2

    def sync_config(self, c):
        self._charge = c.charge
        self._startup = 4 / 60
        self._recovery = 59 / 60
        self._active = c.active

    def getstartup(self):
        startup = self._startup_a
        startup += self._charge / self.fs_speed
        startup += self._startup / self.speed()
        return startup

    def __call__(self, before):
        if type(before).__name__ == 'FS_Speedable':
            self._startup_a = 88 / 60
        elif type(before).__name__ == 'X':
            if now()-before.startup_start > 0:
                if before.name == 'x1' and self.fs_speed == 1.2:
                    self._startup_a = 3 / 60
                else:
                    self._startup_a = 0
            else:
                return self(before.getprev())
        elif type(before).__name__ == 'S':
            self._startup_a = 0
        elif type(before).__name__ == 'Dodge':
            self._startup_a = 14 / 60
        return self.tap()

class Hunter_Sarisse(Adv):
    comment = 'fs hit count vary on distance and enemy size; needs combo time from chain coability to keep combo'
    a1 = ('fs', 0.30)
    a3 = ('fs', 0.25)

    conf = {}
    conf['slots.a'] = Stellar_Show()+Primal_Crisis()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['slots.d'] = Dragonyule_Jeanne()
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `dodge, fsc
        `fs4
    """
    coab = ['Dagger', 'Xander', 'Grace']

    def init(self):
        default_pierce = 2 if self.condition('lance+ distance from HBH sized enemy') else 1
        conf_alt_fs = {
            'fs1': {
                'dmg': 0.74,
                'sp': 500,
                'charge': 29 / 60.0,
                'recovery': 4 / 60.0,
                'hit': 3,
                'pierce': default_pierce
            },
            'fs2': {
                'dmg': 0.84,
                'sp': 710,
                'charge': (29+43) / 60.0,
                'hit': 3,
                'pierce': default_pierce
            },
            'fs3': {
                'dmg': 0.94,
                'sp': 920,
                'charge': (29+43*2) / 60.0,
                'hit': 4,
                'pierce': default_pierce
            },
            'fs4': {
                'dmg': 1.29,
                'sp': 1140,
                'charge': (29+43*3) / 60.0,
                'hit': 4,
                'pierce': default_pierce
            }
        }
        for n, c in conf_alt_fs.items():
            self.conf[n] = Conf(c)
            act = FS_Speedable(n, self.conf[n])
            self.s2_spd_boost = act.t_fs_speed
            self.__dict__['a_'+n] = act

        self.l_fs1 = Listener('fs1',self.l_fs1)
        self.l_fs2 = Listener('fs2',self.l_fs2)
        self.l_fs3 = Listener('fs3',self.l_fs3)
        self.l_fs4 = Listener('fs4',self.l_fs4)
        self.fs = None

    def do_fs(self, e, name):
        log('cast','fs')
        self.__dict__['a_'+name].getdoing().cancel_by.append(name)
        self.__dict__['a_'+name].getdoing().interrupt_by.append(name)
        self.fs_before(e)
        fs_hits = 0
        for p in range(self.conf[name+'.pierce']):
            coef = self.conf[name+'.dmg']*(0.3**p)
            coef_name = 'fs' if p == 0 else 'o_fs_extra_{}'.format(p)
            if coef < 0.01:
                break
            for _ in range(self.conf[name+'.hit']):
                self.dmg_make(coef_name, coef, 'fs')
                fs_hits += 1
        self.hits += fs_hits
        self.fs_proc(e)
        self.think_pin('fs')
        self.charge(name,self.conf[name+'.sp'])

    def l_fs1(self, e):
        self.do_fs(e, 'fs1')

    def fs1(self):
        doing = self.action.getdoing()
        return self.a_fs1(doing)

    def l_fs2(self, e):
        self.do_fs(e, 'fs2')

    def fs2(self):
        doing = self.action.getdoing()
        return self.a_fs2(doing)

    def l_fs3(self, e):
        self.do_fs(e, 'fs3')

    def fs3(self):
        doing = self.action.getdoing()
        return self.a_fs3(doing)

    def l_fs4(self, e):
        self.do_fs(e, 'fs4')

    def fs4(self):
        doing = self.action.getdoing()
        return self.a_fs4(doing)

    def prerun(self):
        self.s1_fs_boost = SingleActionBuff('s1', 1.00, 1, 'fs', 'buff', ['fs1','fs2','fs3','fs4'])

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.s1_fs_boost = SingleActionBuff(dst, 1.00, 1, 'fs', 'buff', ['fs','fs1','fs2','fs3','fs4'])

    def s1_proc(self, e):
        self.s1_fs_boost.on()

    def s2_proc(self, e):
        Event('fs_speed_buff')()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)