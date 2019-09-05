if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *

def module():
    return Fleur

class Fleur(Adv):
    comment = 'c4fs; S1, then S1 S2 S3 S1'
    a1 = ('sp',0.08,'hp70')
    a3 = ('k_paralysis',0.2)
    

    conf = {}
    conf['acl'] = """
        `s2, s=1
        `s3, s=2
        `s1 
        `fs, seq=4
    """

    def init(this):
        this.s1_stance = 1

    def getbane(this):
        return this.afflics.paralysis.get()*0.2

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.paralysis.resist=0
        else:
            this.afflics.paralysis.resist=100



    def s1_proc(this, e):
        coef = 3.33
        this.dmg_make('s1', coef)
        coef = 3.33*0.8 * this.afflics.paralysis.get()
        this.dmg_make('o_s1_boost', coef)

        if this.s1_stance == 1:
            this.afflics.paralysis('s1',110, 0.883)
            this.s1_stance = 2
        elif this.s1_stance == 2:
            this.afflics.paralysis('s1',160, 0.883)
            this.s1_stance = 3
        elif this.s1_stance == 3:
            this.afflics.paralysis('s1',160, 0.883)
            this.s1_stance = 1

        coef = 3.33
        this.dmg_make('s1', coef)
        coef = 3.33*0.8 * this.afflics.paralysis.get()
        this.dmg_make('o_s1_boost', coef)


    def s2_proc(this, e):
        this.s1.charge(this.s1.sp)



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)




