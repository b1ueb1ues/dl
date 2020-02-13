import adv.adv_test
import adv
from slot.a import *

def module():
    return Aoi

class Aoi(adv.Adv):
    a1 = ('od',0.15)
    conf = {}
    conf['slot.a'] = RR()+EE()
    conf['acl'] = """
        `s3, not this.s3_buff_on 
        `s1
        `s2
        """
    conf['afflict_res.burn'] = 0

    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)
    
    def s2_proc(this, e):
        this.afflics.burn('s2',100,0.803)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

