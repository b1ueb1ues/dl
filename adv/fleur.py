import adv_test
from adv import *

def module():
    return Fleur

class Fleur(Adv):
    comment = 'don\'t use s2 in s3 nor s3 in s2'
    conf = {}
    a1 = ('sp',0.08,'hp70')
    
    def pre(this):
        if this.condition('paralysis 40s (s1 boosted when)'):
            this.init, this.o_init = this.c_init, this.init


    def init(this):
        this.ss = Selfbuff('paralysis killer',0.2,40,'att','killer') # is off

    def c_init(this):
        #this.dmg_make("o_s1hitpara",(5.994*1.2-3.33)*2)
        #this.dmg_make("o_s1hitpara",(5.994*1.2-3.33)*2)
        #this.dmg_make("o_s1hitpara",(5.994*1.2-3.33)*2)
        #this.dmg_make("o_s1hitpara",(5.994*1.2-3.33)*2)
        this.dmg_make("o_s1_para",(0.883*3*4))
        this.ss = Selfbuff('paralysis killer',0.2,40,'att','killer').on()

    def s1_proc(this, e):
        if this.ss.get():
            this.dmg_make("o_s1hitpara",(5.994-3.33)*2)

    def s2_proc(this, e):
        this.s1.charge(this.s1.sp)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s3,s1.charged>=s1.sp and seq=4
        `s1, seq=5
        `s1, s=2
        `s2, sx=1
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)




