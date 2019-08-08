if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

from adv import *
from adv import sazanka
from module.bleed import mBleed
from slot.d import *
from slot.a import *

def module():
    return Sazanka

class Sazanka(sazanka.Sazanka):
    def prerun(this):
        this.bleed = mBleed("g_bleed",0).reset()
        this.s2fscharge = 0

    def s1_proc(this, e):
        mBleed("s1_bleed", 1.32).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3, fsc
        `s2, fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, mass=0)
