import adv_test
from adv import *
from slot.a import *

def module():
    return Renelle

class Renelle(Adv):
    a1 = ('cc',0.15,'hit15')

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
    conf['slot.a'] = TB()+EE()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, cancel
        `s2, cancel
        `fs, x=5
        """
    adv_test.test(module(), conf, verbose=-2)

