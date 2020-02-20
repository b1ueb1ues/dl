import adv.adv_test
from core.advbase import *
from core.advbase import *
from slot.a import *

def module():
    return Naveed

class Naveed(Adv):
    a1 = ('a',0.08,'hit15')
    a3 = ('prep','100%')
    conf = {}
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s2, this.s1level < 5
        `s1
        `fs, seq=3 and cancel
        """
    conf['slot.a'] = TSO()+Primal_Crisis()
            
    def prerun(this):
        this.s1level = 0

    def s1_proc(this, e):
        for _ in range(this.s1level):
            for _ in range(3):
                this.dmg_make("o_s1_boost",0.7,'s')
                this.hits += 1

    def s2_proc(this, e):
        this.s1level += 1
        if this.s1level >= 5:
            this.s1level = 5
        adv.Event('defchain')()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

