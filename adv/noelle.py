import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *


def module():
    return Noelle

class Noelle(Adv):
    a1 = ('bt',0.25)
    a3 = ('primed_defense',0.08)

    conf = {}
    conf['slots.d'] = Freyja()
    conf['slots.a'] = A_Dogs_Day()+Castle_Cheer_Corps()

    conf['acl'] = """
        `s1
        `fs, self.fs_prep_c==3 and s1.charged>=s1.sp*1/2-self.sp_val('fs')
        `fs, self.fs_prep_c==1 and s1.charged>=s1.sp*3/4-self.sp_val('fs')
        `s2, x=5
        `s3, x=5
        """

    def init(self):
        if self.condition('buff all team'):
            self.s1_proc = self.c_s1_proc

    def c_s1_proc(self, e):
        Teambuff('s1',0.25,15).on()

    def s1_proc(self, e):
        Selfbuff('s1',0.25,15).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

