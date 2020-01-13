import adv_test
from adv import *
from module.bleed import Bleed
from slot.a import *

def module():
    return Ieyasu

class Ieyasu(Adv):
    a1 = ('cc',0.13,'hp70')
    a2 = ('cd',0.3)

    comment = 'no poison'

    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5 and this.bleed._static['stacks'] > 0
        `s3
        """

    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = RR()+BN()
        else:
            this.conf.slot.a = RR()+JotS()

    def s2ifbleed(this):
        if this.s2buff.get()!=0:
            if this.bleed._static['stacks'] > 0:
                return 0.20
        return 0

    def prerun(this):
        random.seed()
        this.s2buff = Selfbuff("s2",0.20,15,'crit')
        this.s2buff.modifier.get = this.s2ifbleed
        this.bleed = Bleed("g_bleed",0).reset()
        this.s2charge = 0
        this.poisoned = False

    def s1_proc(this, e):
        if this.poisoned:
            coef = 0.31*8
            this.dmg_make("o_s1_boost", coef)
            Bleed("s1_bleed", 1.752).on()
        else:
            Bleed("s1_bleed", 1.46).on()

    def s2_proc(this, e):
        this.s2buff.on()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)
