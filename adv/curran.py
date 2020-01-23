import adv_test
from adv import *
from slot.d import *
from slot.a import *


def module():
    return Curran

class Curran(Adv):
    comment = "no fs"

    a1 = ('od',0.15)
    a3 = ('lo',0.6)

    conf = {}
    conf['slot.a'] = KFM()+CE()

    def s1_proc(this, e):
        with Modifier("s1killer", "poison_killer", "hit", 0.6):
            this.dmg_make("s1", 14.70)

    def s2_proc(this, e):
        with Modifier("s2killer", "poison_killer", "hit", 1):
            this.dmg_make("s2", 12.54)

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=2
        `s3, seq=5
        """
    conf['slot.d'] = Shinobi()
    adv_test.test(module(), conf, verbose=-2)
