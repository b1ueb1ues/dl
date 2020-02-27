import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Nefaria

class Nefaria(Adv):
    a1 = ('k_poison',0.3)
    a3 = ('k_blind',0.4)
    conf = {}
    conf['slot.d'] = Shinobi()
    conf['slot.a'] = Dear_Diary()+The_Fires_of_Hate()
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, x=4
        """
    conf['afflict_res.blind'] = 80
    conf['afflict_res.poison'] = 0

    def prerun(this):
        this.s2fscharge = 0
        if this.condition('hp100'):
            this.fullhp = 1
        else:
            this.fullhp = 0

    def s1_proc(this, e):
        coef = min(1, this.afflics.poison.get() + this.afflics.blind.get())
        with Modifier('s1killer', 'att', 'hit', 0.74*coef):
            this.afflics.poison('s1', 120+this.fullhp*60, 0.582)
            this.dmg_make('s1',8*1.06)

    def s2_proc(this, e):
        this.s2fscharge = 1

    def fs_proc(this, e):
        if this.s2fscharge > 0:
            this.s2fscharge -= 1
            this.dmg_make('o_fs_boost', 0.48)
            this.afflics.blind('s2_fs', 100+this.fullhp*60)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)