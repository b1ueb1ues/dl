if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return W_Elisanne


class W_Elisanne(Adv):
    conf = {}
    conf['slot.a'] = First_Rate_Hospitality() + The_Shining_Overlord()
    conf['acl'] = """
        `s1,fsc
        `s2
        `s3,fsc
        `fs, seq=3 and cancel
    """

    a1 = ('sp',0.08)
    a3 = ('bc',0.13)

    def prerun(this):
        if this.condition('s2 defdown for 10s'):
            this.s2defdown = 1
        else:
            this.s2defdown = 0


    def s2_proc(this, e):
        if this.s2defdown :
            Debuff('s2defdown',0.15,10,1).on()


    def s3_proc(this, e):
        Event('defchain')()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2, mass=0)
