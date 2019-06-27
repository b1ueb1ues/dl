import adv_test
from adv import *
from module.bleed import Bleed
from slot.a import *

from slot import *
class blade(WeaponBase):
    ele = ['wind']
    wt = 'blade'
    att = 372 
    a = [('k',0.3), ('prep','50%')]
    conf = {}


def module():
    return Addis



class Addis(Adv):
    comment = 's2 c2 s1 c5 fsf c4 fs s1'
    a3 = ('bk',0.20)

    def getbleedpunisher(this):
        if this.bleed._static['stacks'] > 0:
            return 0.08
        return 0

    def init(this):
        random.seed()
        this.poisoncount=3
        this.s2buff = Selfbuff("s2_shapshifts1",1, 10,'ss','ss')
        this.s2str = Selfbuff("s2_str",0.25,10)
        this.bleedpunisher = Modifier("bleed","att","killer",0.08)
        this.bleedpunisher.get = this.getbleedpunisher
        this.bleed = Bleed("g_bleed",0).reset()
        #this.crit_mod = this.rand_crit_mod


    def s1_proc(this, e):

        if this.s2buff.get():
            this.s2buff.buff_end_timer.timing += 2.5
            this.s2str.buff_end_timer.timing += 2.5
            log('-special','s1_with_s2')
            if random.random() < 0.8:
                Bleed("s1_bleed", 1.32).on()
            else:
                log('-special','s1_bleed_failed')
        else:
            if this.poisoncount > 0:
                this.poisoncount -= 1
                this.dmg_make("o_s1_poison",2.65)


    def s2_proc(this, e):
        this.s2buff.on()
        this.s2str.on()


if __name__ == '__main__':
    conf = {}
    #conf['slot.w'] = blade()
    #conf['slots.a'] = Evening_of_Luxury() + RR()
    #conf['mod'] = {'wand':('s','ex',0.15),'blade':('a','ex',0.1)}

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
    adv_test.test(module(), conf,verbose=0, mass=1)

