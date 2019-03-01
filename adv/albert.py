import adv_test
from adv import *
import copy
from module.fsalt import *


def module():
    return Albert


class Albert(Adv):
    conf = {
            'mod_a':('fs','passive',0.5),
            #'mod_wp':('s','passive',0.35),
            }

    def init(this):
        this.fsa_conf = copy.deepcopy(this.conf)
        this.fsa_conf.update( {
                'fs_dmg':1.02,
                'fs_sp':330,
                'fs_recovery':26/60.0,
                'x1fs_recovery':26/60.0,
                })
        this.s2timer = Timer(this.s2autocharge,1,1).on()
        this.paralyze_count=3
        this.s2buff = Buff("s2_shapshift",1, 20,'ss','ss','self')
        this.a2buff = Buff('a2_str_passive',0.25,20,'att','passive','self')

        this.fsalttimer = Timer(this.altend)
        fs_alt_init(this, this.fsa_conf)

    def altend(this,t):
        fs_back(this)


    def s2autocharge(this, t):
        if not this.a2buff.get():
            this.s2.charge(160000.0/40)
            log('sp','s2autocharge')

            
    def condition(this):
        this.conf['acl'] = """
            `s2, s1.charged>=s1.sp
            `s1
            `s3, not this.s2buff.get()
            `fs, seq=3 
            """
        return '3s1 in one s2'


    def s1_proc(this, e):
        if this.s2buff.get():
            this.dmg_make("o_s1_s2boost",12.38-0.825+0.83*5)


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
        `fs, seq=2
        """
    adv_test.test(module(), conf,verbose=0, mass=0)

