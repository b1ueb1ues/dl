import adv.adv_test
from adv import *

def module():
    return Hawk

class Hawk(Adv):
    def init(this):
        this.s2fscharge = 0
        if this.condition('fullhp=stun'):
            this.fullhp = 1
        else:
            this.fullhp = 0
        if this.condition('80 resist'):
            this.afflics.stun.resist=80
        else:
            this.afflics.stun.resist=100


    def prerun(this):
        this.m = Modifier('skiller','att','killer',0.3)
        this.m.get = this.getbane

        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """

    def getbane(this):
        return this.afflics.stun.get()*0.3

    def s1_before(this, e):
        r = this.afflics.stun.get()
        coef = 8.48 * (1-r)
        return coef

    def s1_proc(this, e):
        r = this.afflics.stun.get()
        coef = 8.48 * r
        this.dmg_make('s1',coef)
        coef = (18.232-8.48) * r
        this.dmg_make('o_s1_boost',coef)


    def s2_proc(this, e):
        this.s2fscharge = 3

    def fs_proc(this, e):
        if this.s2fscharge > 0:
            this.s2fscharge -= 1
            this.dmg_make("o_s2_fs",0.48)
            this.afflics.stun('s2_fs', 100+this.fullhp*60, 5.5)



if __name__ == '__main__':
    #module().comment = 'boost dmg from stun 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

