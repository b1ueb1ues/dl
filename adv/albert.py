import adv_test
from adv import *
import copy
from module.fsalt import *


def module():
    return Albert


class Albert(Adv):
    a1 = ('fs',0.5)

    def init(this):
        this.fsaconf = Conf()
        this.fsaconf.fs = Conf(this.conf.fs)
        this.fsaconf( {
                'fs.dmg':1.02,
                'fs.sp':330,
                'fs.recovery':26/60.0,
                'x1fs.recovery':26/60.0,
                })
        this.s2timer = Timer(this.s2autocharge,1,1).on()
        this.paralyze_count=3
        this.s2buff = Selfbuff("s2_shapshift",1, 20,'ss','ss')
        this.a2buff = Selfbuff('a2_str_passive',0.25,20,'att','passive')

        this.fsalttimer = Timer(this.altend)
        fs_alt_init(this, this.fsaconf)

    def altend(this,t):
        fs_back(this)


    def s2autocharge(this, t):
        if not this.a2buff.get():
            this.s2.charge(160000.0/40)
            log('sp','s2autocharge')

            
    def pre(this):
        if this.condition('3s1 in on s2'):
            this.conf['acl'] = """
                `s2, s1.charged>=s1.sp-300
                `s1
                `s3, not this.s2buff.get()
                `fs, seq=2 
                """
        if this.condition('big hitbox'):
            this.s1_proc = this.c_s1_proc


    def c_s1_proc(this, e):
        if this.s2buff.get():
            this.dmg_make("o_s1_s2boost",12.38-0.825+0.83*5)
    

    def s1_proc(this, e):
        if this.s2buff.get():
            this.dmg_make("o_s1_s2boost",12.38-0.825+0.83*1)


    def fs_proc(this, e):
        if this.paralyze_count > 0:
            if this.s2buff.get():
                this.paralyze_count -= 1
                this.dmg_make("o_s1_paralyze",0.803*3)

    def s2_proc(this, e):
        this.s2timer.on()
        this.s2buff.on()
        this.a2buff.on()
        fs_alt(this)
        this.fsalttimer(20)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2
        `s1, this.s2.charged > 900
        `s3
        `fs, seq=2 and not this.s2buff.get()
        """
    adv_test.test(module(), conf,verbose=0, mass=0)

