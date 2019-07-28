import adv_test
from adv import *
from adv import addis
from module.bleed import mBleed
from slot.a import *

def module():
    return Addis

class Addis(addis.Addis):
    def prerun(this):
        this.poisoncount=3
        this.s2buff = Selfbuff("s2_shapshifts1",1, 10,'ss','ss')
        this.s2str = Selfbuff("s2_str",0.25,10)
        this.bleedpunisher = Modifier("bleed","att","killer",0.08)
        this.bleedpunisher.get = this.getbleedpunisher
        this.bleed = mBleed("g_bleed",0).reset()


    def s1_proc(this, e):
        if this.s2buff.get():
            this.s2buff.buff_end_timer.timing += 2.5
            this.s2str.buff_end_timer.timing += 2.5
            log('-special','s1_with_s2')
            mBleed("s1_bleed", 1.32).on()
        else:
            if this.poisoncount > 0:
                this.poisoncount -= 1
                this.dmg_make("o_s1_poison",2.65)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        # bs = this.bleed._static['stacks']
        `s2, s1.charged>=s1.sp-260 and seq=5 and bs != 3
        `s1, s2.charged<s2.sp and bs != 3
        `s3, not this.s2buff.get()
        `fs, this.s2buff.get() and seq=4 and this.s1.charged>=s1.sp-200
        """

   # conf['acl'] = """
   #     `s2, s1.charged>=s1.sp-260 and seq=5
   #     `s1, s2.charged<s2.sp
   #     `s3, not this.s2buff.get()
   #     `s3, s2.sp > 2000 and sx=1
   #     `fs, this.s2buff.get() and seq=5
   #     """
    adv_test.test(module(), conf,verbose=0, mass=0)

