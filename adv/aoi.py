import adv_test
import adv
from slot.a import *

def module():
    return Aoi

class Aoi(adv.Adv):
    a1 = ('od',0.15)

    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)
    
    def s2_proc(this, e):
        this.afflics.burn('s2',90,0.6)

if __name__ == '__main__':
    conf = {}
    conf['slot.a'] = RR()+EE()
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)

