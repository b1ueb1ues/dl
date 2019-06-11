import adv_test
from adv import *

def module():
    return Vida

class Vida(Adv):
#    comment = 'unsuitable resist'
    a1 = ('fs',0.30)

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
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

