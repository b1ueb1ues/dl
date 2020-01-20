import adv_test
from adv import *

def module():
    return Nefaria

class Nefaria(Adv):
    a3 = ('k_blind',0.3)
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
    """

    def prerun(this):
        if this.condition('80 resist'):
            this.afflics.blind.resist=80
        else:
            this.afflics.blind.resist=100
        this.s2fscharge = 0
        if this.condition('fullhp=blind'):
            this.fullhp = 1
        else:
            this.fullhp = 0

    def s1_proc(this, e):
        with Modifier("s1killer", "blind_killer", "hit", 0.74):
            this.dmg_make('s1',8*1.06)

    def s2_proc(this, e):
        this.s2fscharge = 3

    def fs_proc(this, e):
        if this.s2fscharge > 0:
            this.s2fscharge -= 1
            this.dmg_make("o_fs_boost",0.48)
            this.afflics.blind('s2_fs', 100+this.fullhp*60)




if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

