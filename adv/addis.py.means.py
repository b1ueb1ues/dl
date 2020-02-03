import adv.adv_test
from adv import *
from adv import addis
from module.bleed import mBleed
from slot.a import *

def module():
    return Addis

class Addis(addis.Addis):
    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.poison.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.poison.resist=100

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
            this.afflics.poison('s1',100,0.53)



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf,verbose=0, mass=0)

