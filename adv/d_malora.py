import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return D_Malora

class D_Malora(Adv):
    comment = 'c4fsf c5 c4 s1'
    a1 = ('od',0.13)

    conf = {}
    conf['slot.a'] = KFM()+FitF()
    conf['acl'] = """
        `s1
        `s2, this.mod('def')!=1
        `fsf, x=4 and (s1.charged == this.sp_val(4))
        """

    def prerun(this):
        if this.condition('buff all team'):
            this.s1debuff = Debuff('s1',0.15,15)
        else:
            this.s1debuff = False

    def s1_proc(this, e):
        if this.s1debuff:
            this.s1debuff.on()
        this.dmg_make('s1',4.67,'s')
        this.hits += 1

    def s2_proc(this, e):
        if this.mod('def')!= 1:
            this.dmg_make('o_s2_boost',4.32*3*0.8)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

