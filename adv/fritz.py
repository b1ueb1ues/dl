import adv_test
import adv
from adv import *

def module():
    return Fritz

class Fritz(adv.Adv):

    def init(this):
        this.stance = 0
        this.s2fscharge = 0

    def s1_proc(this, e):
        Buff('defdown',-0.02,10,'def').on()

    def s2_proc(this, e):
        this.s2fscharge = 3

    def fs_proc(this, e):
        if this.s2fscharge > 0:
            this.s2fscharge -= 1
            this.dmg_make("o_s2fs",0.57*3+0.29)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    adv_test.test(module(), conf, verbose=0)
