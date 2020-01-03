import adv_test
import adv
from slot.a import *
from slot.d import *

def module():
    return Euden

class Euden(adv.Adv):
    conf ={}
    conf['slot.a'] = TSO()+EE()
    a1 = ('dc', 0.10)

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.burn.resist=0
        else:
            this.afflics.burn.resist=100

    def s1_proc(this, e):
        this.afflics.burn('s1',110,0.883)

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=-2)

