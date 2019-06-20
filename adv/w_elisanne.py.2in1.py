import adv_test
from adv import *
from slot.a import *

def module():
    return W_Elisanne


class W_Elisanne(Adv):
    comment = 'FRH+JotS and 2in1'

    conf = {}
#    conf['slot.a'] = First_Rate_Hospitality() + The_Shining_Overlord()
    conf['slot.a'] = JotS() + The_Shining_Overlord()

    a1 = ('sp',0.08)
    a3 = ('bc',0.13)

    def init(this):
        this.s2on = 0
        if this.condition('s2 defdown for 10s'):
            this.s2defdown = 1
        else:
            this.s2defdown = 0


    def s2_proc(this, e):
        if this.s2defdown :
            Debuff('s2defdown',0.15,10,1).on()
        this.s2on = 1
        Timer(this.s2off).on(10);

    def s2off(this, t):
        this.s2on = 0


    def s3_proc(this, e):
        Event('defchain')()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, fsc
        `s1, fsc
        `s3, fsc
        `fs, seq=3 and cancel 
    """

    adv_test.test(module(), conf, verbose=-2, mass=0)
