import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Lea

class Lea(Adv):
    comment = 'c2+fs; no s2'
    a1 = ('fs', 0.50)
    a3 = ('sp', 0.12, 'fs')
    
    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.burn.resist=0
        else:
            this.afflics.burn.resist=100
    
    def s1_proc(this, e):
        this.afflics.burn('s1',120,0.97)

if __name__ == '__main__':
    conf = {}
    conf['slot.d'] = Apollo()
    conf['slot.a'] = TSO()+EE()
    conf['acl'] = """
        `s1, fsc
        `s3, fsc
        `fs, seq=2
        """

    adv_test.test(module(), conf, verbose=0, mass=0)
