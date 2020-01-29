import adv_test
import adv
from slot.a import *
from slot.d import *

def module():
    return Xania

class Xania(adv.Adv):
    a1 = ('s',0.35)
    #comment = 'reach 100 resist with Saintly Delivery'
    #conf = {}
    #import slot
    #conf['slots.a'] = slot.a.Saintly_Delivery()+slot.a.RR()

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.burn.resist=0
        else:
            this.afflics.burn.resist=100
    
    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)
    
    def s2_proc(this, e):
        this.afflics.burn('s2',100,0.803)

if __name__ == '__main__':
    conf = {}
    conf['slot.d'] = Apollo()
    conf['acl'] = """
        `s1
        `s2
        `s3
        """
    adv_test.test(module(), conf, verbose=-2)
