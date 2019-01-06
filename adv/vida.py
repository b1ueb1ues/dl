import adv_test
from adv import *

def module():
    return Vida

class Vida(Adv):
    conf = {
        "mod_a"   : ('fs', 'passive', 0.30)
        } 

    def init(this):
        this.s2charge = 0

    def s2_proc(this, e):
        this.s2charge = 3

    def fs_proc(this, e):
        if this.s2charge > 0:
            this.s2charge -= 1
            this.dmg_make("o_s2fs",0.21*3)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `fs, seq=5
        `s1, seq=5 and cancel 
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

