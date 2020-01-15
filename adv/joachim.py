if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Joachim

class Joachim(Adv):
    comment = ''
    a1 = ('a',0.10,'hp70')
    a3 = ('k_poison',0.2)
    
    conf = {}
    conf['slot.a'] = Dear_Diary() + TP()
    conf['slot.d'] = Vayu()
    conf['acl'] = """
        `s2, s=1
        `s1
        `s3
    """

    def init(this):
        this.s1_stance = 1

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.poison.resist=0
        else:
            this.afflics.poison.resist=100

    def s1_proc(this, e):
        if this.s1_stance == 1:
            this.afflics.poison('s1',110, 0.53)
            this.s1_stance = 2
        elif this.s1_stance == 2:
            this.afflics.poison('s1',160, 0.53)
            this.s1_stance = 3
        elif this.s1_stance == 3:
            Teambuff("s1atk",0.15,10).on()
            this.afflics.poison('s1',160, 0.53)
            this.s1_stance = 1

        coef = 2.2
        this.dmg_make('s1', coef)
        coef = 2.2*0.8 * this.afflics.poison.get()
        this.dmg_make('o_s1_boost', coef)


    def s2_proc(this, e):
        this.s1.charge(this.s1.sp)



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)




