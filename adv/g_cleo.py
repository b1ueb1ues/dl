from core.advbase import *
from slot import *
from slot.w import *
from slot.a import *
from slot.d import *
from module.x_alt import Fs_alt

import random
random.seed()


def module():
    return Gala_Cleo

class Gala_Cleo(Adv):
    comment = '(the true cleo is here)'
    a3 = ('prep','100%')
    conf = {}
    conf['slot.a'] = CC()+JotS()  # wand c2*1.08 = 217
    conf['slot.d'] = Shinobi()
    conf['acl'] = """
        `s3, pin='prep'
        `fs, s1.charged>=s1.sp and self.fs_alt.uses > 0
        `s2, x=5 or x=4 or fsc or s=3
        `s1, s=2 or fsc
        """

    def d_slots(self):
        if 'bow' in self.ex:
            self.slots.a = CC()+Primal_Crisis()

    def fs_proc_alt(self, e):
        if self.a1_buffed:
            buff = Teambuff('a1_str',0.25,10)
            buff.bufftime = buff.nobufftime
            buff.on()

    def prerun(self):
        self.a1_buffed = self.condition('always in a1')
        self.s1p = 0 

        conf_fs_alt = {
            'fs.dmg':0,
            'fs.sp' :0,
            'fs.charge': 30/60.0,
            'fs.startup': 20/60.0,
            'fs.recovery': 60/60.0,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)

    def s1_dmg(self, t):
        self.dmg_make('s1',0.88)
        self.hits += 1
        self.dmg_make('s1',2.65)
        self.hits += 1

    def s1_proc(self, e):
        self.s1p += 1
        if self.s1p > 3 :
            self.s1p = 1
        if self.s1p == 1:
            Timer(self.s1_dmg).on((42.0 + 12*0 )/60)
            Timer(self.s1_dmg).on((42.0 + 12*1 )/60)
            Timer(self.s1_dmg).on((42.0 + 12*2 )/60)
        elif self.s1p == 2:
            Timer(self.s1_dmg).on((42.0 + 12*0 )/60)
            Timer(self.s1_dmg).on((42.0 + 12*1 )/60)
            Timer(self.s1_dmg).on((42.0 + 12*2 )/60)
            Timer(self.s1_dmg).on((42.0 + 12*3 )/60)
        elif self.s1p == 3:
            Timer(self.s1_dmg).on((42.0 + 12*0 )/60)
            Timer(self.s1_dmg).on((42.0 + 12*1 )/60)
            Timer(self.s1_dmg).on((42.0 + 12*2 )/60)
            Timer(self.s1_dmg).on((42.0 + 12*3 )/60)
            Timer(self.s1_dmg).on((42.0 + 12*4 )/60)

        self.fs_alt.on()

    def s2_proc(self, e):
        Debuff('s2', 0.10, 20).on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)