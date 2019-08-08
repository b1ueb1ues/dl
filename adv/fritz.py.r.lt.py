import adv.adv_test
import adv
from adv import *

def module():
    return Fritz

class Fritz(adv.Adv):

    def prerun(this):
        this.stance = 0
        this.s2fscharge = 0

    def s2_proc(this, e):
        this.s2fscharge = 3

    def fs_proc(this, e):
        if this.s2fscharge > 0:
            this.s2fscharge -= 1
            this.dmg_make("o_s2fs",0.57*3+0.29)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `rotation
    """
    conf['rotation_init'] = """
        C4FSc4fs C2-
    """
    conf['rotation'] = """
        s1
        C4FSc4fs C2- S1 C2- S2 C4FS C4- S3 C3- S1
        C2FSc2fs C4FS C2-
        S1 C3- S2
        C2FSc2fsc2fs C2- S1
        C4FSc4fs C5- S2 C3- S3 C1FS- S1 C1FS C1FS C4FS C3-
    """

    adv_test.test(module(), conf, verbose=0)
