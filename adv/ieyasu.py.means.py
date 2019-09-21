if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from adv import ieyasu
from module.bleed import mBleed
import slot

def module():
    return Ieyasu

class Ieyasu(ieyasu.Ieyasu):
    def prerun(this):
        this.s2buff = Selfbuff("s2",0.15, 15, 'crit')
        this.s2buff.modifier.get = this.s2ifbleed
        this.bleed = mBleed("g_bleed",0).reset()
        this.s2charge = 0

    def s1_proc(this, e):
        mBleed("s1_bleed", 1.46).on()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=1, mass=0)
