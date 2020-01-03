import adv_test
from adv import *
from slot.a import *

def module():
    return Alain

class Alain(Adv):
    #comment = 'reach 100 resist with Saintly Delivery'
    #conf = {
    #        'slots.a': RR()+Saintly_Delivery()
    #    }
    
    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.burn.resist=0
        else:
            this.afflics.burn.resist=100

    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)
    
    def s2_proc(this, e):
        this.afflics.burn('s1',100,0.803)

if __name__ == '__main__':
    conf = {}
    conf['slot.a'] = RR()+EE()
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

