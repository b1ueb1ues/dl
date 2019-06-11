import adv_test
from adv import *
from module.bleed import Bleed
from slot.a import *

def module():
    return Botan

class Botan(Adv):
#    comment = "RR+Jewels"
    a3 = ('prep','50%')
    conf = {}
    conf['slots.a'] = RR() + Jewels_of_the_Sun()

    def init(this):
        this.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(this, e):
        if random.random() < 0.8:
            Bleed("s1_bleed", 1.32).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2,mass=1)


