from core.advbase import *
from slot.a import *
from slot.d import *
from module.x_alt import Fs_alt

def module():
    return Zena

class Zena(Adv):
    comment = '40 extra hits s2 on Agito size enemy (max 100 without roll & 120 with roll)'
    a1 = ('a', 0.08)
    a3 = ('prep', 100)

    conf = {}
    conf['slots.a'] = Candy_Couriers()+Primal_Crisis()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s2
        `s1
        `s4

        # If healing FS is needed
        # `fs, s1.check() and self.fs_alt.uses>0
        # `s3, not self.s3_buff
        # `s2
        # `s4
        # `s1, fsc or self.fs_alt.uses=0
        """
    coab = ['Blade', 'Dagger', 'Bow']
    share = ['Curran']

    def prerun(self):
        conf_fs_alt = {
            'fs.dmg':0,
            'fs.sp' :0,
            'fs.charge': 30/60.0,
            'fs.startup': 20/60.0,
            'fs.recovery': 60/60.0,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt))
        self.s2_extra_hit_rate = 8 # number of hits per second
        self.s2_timers = []
        Event('dragon').listener(self.s2_clear)

    def prerun_skillshare(self, dst):
        self.fs_alt = Dummy()

    def s1_proc(self, e):
        self.fs_alt.on(1)

    def s2_extra_hits(self, t):
        self.dmg_make(f'{t.name}_extra', self.s2_extra_hit_rate*0.50)
        self.hits += self.s2_extra_hit_rate

    def s2_clear(self, e):
        for t in self.s2_timers:
            t.off()

    def s2_proc(self, e):
        self.s2_clear(e)
        for i in range(0, 5):
            t = Timer(self.s2_extra_hits)
            t.name = e.name
            t.on(i)
            self.s2_timers.append(t)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
