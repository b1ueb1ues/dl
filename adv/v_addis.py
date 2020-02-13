import adv.adv_test
import adv
from slot.d import *
from slot.a import *

def module():
    return Valentines_Addis

class Valentines_Addis(adv.Adv):
    a1 = ('k_poison',0.3)
    conf = {}
    conf['slot.d'] = Shinobi()
    conf['acl'] = """
        `s1
        `s2, not this.a3spd.get()
        `s3
        `fs, x=4
        """

    def init(this):
        this.hp = 100

    def prerun(this):
        this.a3atk = adv.Selfbuff('a3atk',0.20,-1,'att','passive')
        this.a3spd = adv.Spdbuff('a3spd',0.10,-1)

    def s1_proc(this, e):
        with adv.CrisisModifier('s1', 2, this.hp):
            this.afflics.poison('s1', 120, 0.582)
            this.dmg_make('o_s1_crisis', this.conf.s1.dmg)

    def s2_proc(this, e):
        if this.hp > 30:
            this.hp = 20
            this.a3atk.on()
            this.a3spd.on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


