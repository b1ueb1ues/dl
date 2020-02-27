import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Xainfried

class Xainfried(Adv):
    a1 = ('dc', 4)
    a3 = ('dt', 0.25)
    conf = {}
    conf['slot.d'] = Leviathan()
    conf['slot.a'] = Resounding_Rendition()+An_Ancient_Oath()
    conf['acl'] = """
        `dragon
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    conf['afflict_res.frostbite'] = 0

    def s1_proc(this, e):
        with Modifier('s1killer', 'frostbite_killer', 'hit', 0.6):
            this.afflics.frostbite('s1',120,1.00)
            this.dmg_make("s1", 9.20)

    def s2_proc(this, e):
        # unknown gauge amount
        this.dragonform.charge_gauge(10)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

