import adv_test
import adv
from slot.d import *
from slot.a import *


def module():
    return Curran

class Curran(adv.Adv):
    comment = "no fs"

    a1 = ('od',0.15)
    a3 = ('lo',0.6)

    conf = {}
    conf['slot.a'] = KFM()+CE()

    def prerun(this):
        this.poisoned = False

    def s1_proc(this, e):
        if this.poisoned:
            coef = 2.242
            this.dmg_make("o_s1_boost", coef)

    def s2_proc(this, e):
        if this.poisoned:
            coef = 2.256
            this.dmg_make("o_s2_boost", coef)

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=2
        `s3, seq=5
        """
    conf['slot.d'] = Shinobi()
    adv_test.test(module(), conf, verbose=-2)
