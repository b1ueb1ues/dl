import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Alain

class Alain(Adv):
    conf = {}
    conf['slot.a'] = RR()+EE()
    conf['acl'] = """
        `s3, not this.s3_buff
        `s1
        `s2
        `fs, seq=5
        """
    conf['afflict_res.burn'] = 0

    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)
    
    def s2_proc(this, e):
        this.afflics.burn('s1',100,0.803)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

