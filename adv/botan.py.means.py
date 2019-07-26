import adv_test
from adv import *
from module.bleed import mBleed

def module():
    return Botan

class Botan(Adv):
    a3 = ('prep','50%')
    def prerun(this):
        this.bleed = mBleed("g_bleed",0).reset()

    def s1_proc(this, e):
        mBleed("s1_bleed", 1.32).on()


if __name__ == '__main__':
    conf = {}
    from slot.a import *
    conf['slots.a'] = Jewels_of_the_Sun() + RR()
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2,mass=0)


