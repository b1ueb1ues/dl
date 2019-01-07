import adv_test
from adv import *
from module.bleed import Bleed

def module():
    return Sazanka

class Sazanka(Adv):
    comment = 'do not use weapon skill'
    def init(this):
        this.bleed = Bleed("g_bleed",0).reset()
        this.crit_mod = this.rand_crit_mod
        random.seed()
        this.s2fscharge = 0

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
        `s2 
        `fs,seq=5
        """
    adv_test.test(module(), conf, mass=1)

