import adv_test
from adv import *
from module.bleed import Bleed
import slot

def module():
    return Ieyasu

class Ieyasu(Adv):
    comment = "Shinobi"
    #comment = 'RR+Jewels'
    a1 = ('cc',0.1,'hp70')
    a2 = ('cd',0.2)
    conf = {}
    #conf['slots.a'] = slot.a.LC()+slot.a.RR()
    conf['slots.a'] = slot.a.RR()+slot.a.Jewels_of_the_Sun()
    conf['slots.d'] = slot.d.Shinobi()

    def s2ifbleed(this):
        if this.s2buff.get()!=0:
            if this.bleed._static['stacks'] > 0:
                return 0.15
        return 0

    def prerun(this):
        random.seed()
        this.s2buff = Selfbuff("s2",0.15, 15, 'crit')
        this.s2buff.modifier.get = this.s2ifbleed
        this.bleed = Bleed("g_bleed",0).reset()
 #       this.crit_mod = this.rand_crit_mod
        this.s2charge = 0

    def s1_proc(this, e):
        if random.random() < 0.8:
            Bleed("s1_bleed", 1.46).on()


    def s2_proc(this, e):
        this.s2buff.on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5 and this.bleed._static['stacks'] > 0
        `s3
        """
    adv_test.test(module(), conf, verbose=-2, mass=1)

    exit()
    def foo(this, e):
        return
    module().s1_proc = foo
    conf['acl'] = """
        `s1
        `s2, seq=5 and this.bleed._static['stacks'] > 0
        `s3
        """
    adv_test.test(module(), conf, verbose=1, mass=1)
