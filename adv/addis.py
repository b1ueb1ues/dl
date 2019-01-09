import adv_test
from adv import *
from module.bleed import Bleed

def module():
    return Addis

class Addis(Adv):
    def getbleedpunisher(this):
        if this.bleed._static.stacks > 0:
            return 0.08
        return 0

    def init(this):
        this.poisoncount = 3
        #this.s2buff = Buff("s2",0.25, 10, 'att', 'buff','self')
        this.s2buff = Buff("s2_shapshifts1",1, 10,'ss','ss','self')
        this.bleedpunisher = Modifier("bleed","att","punisher",0.08)
        this.bleedpunisher.get = this.getbleedpunisher
        this.bleed = Bleed("g_bleed",0).reset()
        this.crit_mod = this.rand_crit_mod


    def s1_proc(this, e):
        if this.s2buff.get():
            if random.random() < 0.8:
                log('-special','s1_with_s2')
                Bleed("s1_bleed", 1.32).on()
        else:
            if this.poisoncount > 0:
                this.poisoncount -= 1
                this.dmg_make("o_s1_poison",2.65)


    def s2_proc(this, e):
        this.s2buff.on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or s=2
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, mass=1)
