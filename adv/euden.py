import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Euden

class Euden(Adv):
    a1 = ('dc', 0.10)
    conf ={}
    conf['slot.a'] = TSO()+EE()
    conf['slot.d'] = Apollo()
    a1 = ('dc', 0.10)
    
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `fs, seq=3 and cancel
        """
    conf['afflict_res.burn'] = 0

    def s1_proc(this, e):
        this.afflics.burn('s1',110,0.883)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

