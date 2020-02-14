import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Fleur

class Fleur(Adv):
    comment = 'c4fs'
    a1 = ('sp',0.08,'hp70')
    a3 = ('k_paralysis',0.2)

    conf = {}
    conf['slot.a'] = TB()+SotS()
    conf['acl'] = """
        `s2, s=1
        `s1
        `s3
        `fs, seq=4
    """
    conf['afflict_res.paralysis'] = 0

    def init(this):
        this.s1_stance = 1

    def s1_proc(this, e):
        with Modifier("s1killer", "paralysis_killer", "hit", 0.8):
            coef = 3.33
            this.dmg_make('s1', coef)

            if this.s1_stance == 1:
                this.afflics.paralysis('s1',110, 0.883)
                this.s1_stance = 2
            elif this.s1_stance == 2:
                this.afflics.paralysis('s1',160, 0.883)
                this.s1_stance = 3
            elif this.s1_stance == 3:
                this.afflics.paralysis('s1',160, 0.883)
                this.s1_stance = 1

            this.dmg_make('s1', coef)


    def s2_proc(this, e):
        this.s1.charge(this.s1.sp)



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)




