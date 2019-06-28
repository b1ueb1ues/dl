import adv_test
from adv import *
from module.bleed import Bleed
from slot.d import *
from slot.a import *

def module():
    return Sazanka

class Sazanka(Adv):
    comment = 'Shinobi;'
    conf = {}
    conf['slot.d'] = Shinobi()
    conf['slot.a'] = KFM()+CE()

    def init(this):
        this.bleed = Bleed("g_bleed",0).reset()
        this.s2fscharge = 0

    def c_init(this):
        this.o_init()
        Selfbuff('sleep',0.2,14,'att','killer').on()

    def pre(this):
        if this.condition('sleep'):
            this.init, this.o_init = this.c_init, this.init

    def s1_proc(this, e):
        if random.random() < 0.8:
            Bleed("s1_bleed", 1.32).on()

    def s2_proc(this, e):
        this.s2fscharge = 3

    def fs_proc(this, e):
        if this.s2fscharge > 0:
            this.s2fscharge -= 1
            this.dmg_make("o_s2fs",0.38)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3, fsc
        `s2, fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, mass=1)
