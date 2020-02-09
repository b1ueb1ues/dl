import adv.adv_test
import adv
from slot.a import The_Shining_Overlord, Elegant_Escort
from slot.d import Apollo

import sys

def module():
    return Euden

class Euden(adv.Adv):
    a1 = ('dc', 4)
    conf = {}
    conf['slot.d'] = Apollo()
    conf['slot.a'] = The_Shining_Overlord()+Elegant_Escort()
    conf['acl'] = """
        #dragon=this.dragonform
        `dragon, cancel
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `fs, x=3
        """

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.burn.resist=0
        else:
            this.afflics.burn.resist=100

    def s1_proc(this, e):
        this.afflics.burn('s1',110,0.883)
        this.dragonform.charge_gauge(3)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)