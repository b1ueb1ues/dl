import adv_test
from adv import *

def module():
    return Nefaria

class Nefaria(Adv):

    def prerun(this):
        if this.condition('80 resist'):
            this.afflics.blind.resist=80
        else:
            this.afflics.blind.resist=100
        this.m = Modifier('bkiller','att','killer',0.3)
        this.m.get = this.getbane
        this.s2fscharge = 0
        if this.condition('fullhp=blind'):
            this.fullhp = 1
        else:
            this.fullhp = 0

        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """

    def getbane(this):
        return this.afflics.blind.get()*0.3


    def s1_before(this, e):
        r = this.afflics.blind.get()
        coef = 8*1.06 * (1-r)
        return coef

    def s1_proc(this, e):
        r = this.afflics.blind.get()
        coef = 8*1.06 * r
        this.dmg_make('s1',coef)
        coef = 8*(1.8444-1.06) * r
        this.dmg_make('o_s1_boost',coef)

    def s2_proc(this, e):
        this.s2fscharge = 3

    def fs_proc(this, e):
        if this.s2fscharge > 0:
            this.s2fscharge -= 1
            this.dmg_make("o_fs_boost",0.48)
            this.afflics.blind('s2_fs', 100+this.fullhp*60)




if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

