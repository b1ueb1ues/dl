import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Valentines_Addis

class Valentines_Addis(Adv):
    comment = 'use s2 once'

    a1 = ('k_poison',0.3)
    conf = {}
    conf['slot.d'] = Shinobi()
    conf['slot.a'] = The_Plaguebringer()+Primal_Crisis()
    conf['acl'] = """
        `s2, not this.a3atk.get()
        `s1
        `s3
    """
    conf['afflict_res.poison'] = 0

    def prerun(this):
        this.hp = 100
        this.a3atk = Selfbuff('a3atk',0.20,-1,'att','passive')
        this.a3spd = Spdbuff('a3spd',0.10,-1)

    def s1_proc(this, e):
        with CrisisModifier('s1', 1.25, this.hp):
            this.afflics.poison('s1', 120, 0.582)
            this.dmg_make('s1', 8.60)

    def s2_proc(this, e):
        if this.hp > 30:
            this.hp = 20
            this.a3atk.on()
            this.a3spd.on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


