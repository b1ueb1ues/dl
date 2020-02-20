import adv.adv_test
from core.advbase import *
import copy
from module.fsalt import *
from slot.a import *
from slot.d import *

def module():
    return Albert


class Albert(Adv):
    a1 = ('fs',0.5)
    conf = {}
    conf['acl'] = """
        `s2, s1.charged>=s1.sp-330
        `fs, s=2 and not this.afflics.paralysis.get()
        `s1, fsc
        `s3, fsc
        `fs, seq=2
        """
    conf['slot.a'] = TSO()+SDO()
    conf['slot.d'] = C_Phoenix()
    conf['afflict_res.paralysis'] = 0

    def init(this):
        if this.condition('big hitbox'):
            this.s1_proc = this.c_s1_proc

    def prerun(this):
        this.fsaconf = Conf()
        this.fsaconf.fs = Conf(this.conf.fs)
        this.fsaconf( {
                'fs.dmg':1.02,
                'fs.sp':330,
                'fs.recovery':26/60.0,
                'x1fs.recovery':26/60.0,
                })
        this.s2timer = Timer(this.s2autocharge,1,1).on()
        this.s2buff = Selfbuff("s2_shapshift",1, 20,'ss','ss')
        this.a3 = Selfbuff('a2_str_passive',0.25,20,'att','passive')

        this.fsalttimer = Timer(this.altend)
        fs_alt_init(this, this.fsaconf)

    def altend(this,t):
        fs_back(this)

    def s2autocharge(this, t):
        if not this.s2buff.get():
            this.s2.charge(160000.0/40)
            log('sp','s2autocharge')

    def c_s1_proc(this, e):
        if this.s2buff.get():
            this.dmg_make("o_s1_s2boost",12.38-0.825)
            this.dmg_make("o_s1_hit2", 0.83)
            this.dmg_make("o_s1_hit3", 0.83)
            this.dmg_make("o_s1_hit4", 0.83)
            this.dmg_make("o_s1_hit5", 0.83)
            this.dmg_make("o_s1_hit6", 0.83)
            this.s2buff.buff_end_timer.timing += 2.6
            this.a3.buff_end_timer.timing += 2.6
            this.s2timer.timing += 2.6


    def s1_proc(this, e):
        if this.s2buff.get():
            this.dmg_make("o_s1_s2boost",12.38-0.825)
            this.dmg_make("o_s1_hit2", 0.83)
            this.dmg_make("o_s1_hit3", 0.83)
            this.dmg_make("o_s1_hit4", 0.83)
            this.s2buff.buff_end_timer.timing += 2.6
            this.a3.buff_end_timer.timing += 2.6
            this.s2timer.timing += 2.6


    def fs_proc(this, e):
        if this.s2buff.get():
            this.afflics.paralysis('fs',100,0.803)

    def s2_proc(this, e):
        this.s2timer.on()
        this.s2buff.on()
        this.a3.on()
        fs_alt(this)
        this.fsalttimer(20)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

