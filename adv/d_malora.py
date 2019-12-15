import adv_test
from adv import *
from slot.a import *

def module():
    return D_Malora

class D_Malora(Adv):
    a1 = ('od',0.13)

    conf = {}
    conf['slot.a'] = KFM()+FitF()

    def prerun(this):
        if this.condition('buff all team'):
            this.s1debuff = Debuff('s1',0.15,15)
        else:
            this.s1debuff = False

    def s1_proc(this, e):
        if this.s1debuff:
            this.s1debuff.on()
        this.dmg_make('s1',4.67,'s')

    def s2_proc(this, e):
        if this.mod('def')!= 1:
            this.dmg_make('o_s2_boost',4.82*3*0.8)

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=4
        """
    adv_test.test(module(), conf, verbose=-2)

