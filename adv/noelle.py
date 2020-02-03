import adv.adv_test
from adv import *
from slot.d import *
from slot.a import *
from module import energy


def module():
    return Noelle

class Noelle(Adv):
    a1 = ('bt',0.25)
    a3 = ('primed_def',0.08)

    conf = {}
    conf['slots.d'] = Freyja()
    conf['slots.a'] = A_Dogs_Day()+Castle_Cheer_Corps()

    conf['acl'] = """
        `s1
        `fs, this.fs_prep_c==3 and s1.charged>=s1.sp*1/2-this.sp_val('fs')
        `fs, this.fs_prep_c==1 and s1.charged>=s1.sp*3/4-this.sp_val('fs')
        `s2, x=5
        `s3, x=5
        """

    def init(this):
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc

    def c_s1_proc(this, e):
        Teambuff('s1',0.25,15).on()

    def s1_proc(this, e):
        Selfbuff('s1',0.25,15).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

