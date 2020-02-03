import adv.adv_test
from adv import *
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
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s2, fsc
        `s1, fsc
        `fs, seq=2
        """
    conf['cond_afflict_res'] = 0

    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.d = Sakuya()

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100
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
