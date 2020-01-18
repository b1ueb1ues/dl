import adv_test
from adv import *
from slot.a import *
#from slot.d import *

def module():
    return Nobunaga

class Nobunaga(Adv):
    a1 = ('a',0.2,'hit15')
    
    def prerun(this):
        this.ba = 0
    
    def s1_proc(this, e):
        this.ba = 1

    def s2_proc(this, e):
        if this.ba == 1:
            this.ba = 0
            this.dmg_make('o_s1_boost',5.59)

    def fs_proc(this, e):
        if this.ba == 1:
            this.ba = 0
            this.dmg_make('o_s1_boost',5.59)

if __name__ == '__main__':
    conf = {}
    conf['slot.a'] = RR()+FoG()
    #conf['slot.d'] = Cerberus()
    conf['acl'] = """
        `s1
        `s2, cancel
        `fs, x=5 and this.ba=1
        `s3, x=5 or fsc
        """

    adv_test.test(module(), conf, verbose=-2, mass=0)
