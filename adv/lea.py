import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Lea

class Lea(Adv):
    comment = 'c2+fs'
    a1 = ('fs', 0.50)
    a3 = ('sp', 0.12, 'fs')
        
    conf = {}
    conf['slot.a'] = TSO()+EE()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `fs, seq=2
        """
    conf['afflict_res.burn'] = 0
    
    def prerun(this):
        if this.condition('reflect 500 damage on every s2'):
            this.s2reflect = 500
        else:
            this.s2reflect = 0

    def s1_proc(this, e):
        this.afflics.burn('s1',120,0.97)

    def s2_proc(this, e):
        this.dmg_make('o_s2_reflect', this.s2reflect * 11, fixed=True)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0, mass=0)
