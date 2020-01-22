import adv_test
from adv import *
from slot.d import *

def module():
    return Hawk

class Hawk(Adv):
    a3 = ('k_stun',0.3)
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
    """
    conf['slot.d'] = Garland()
    
    def init(this):
        this.s2fscharge = 0
        if this.condition('fullhp=stun'):
            this.fullhp = 1
        else:
            this.fullhp = 0


    def prerun(this):
        if this.condition('80 resist'):
            this.afflics.stun.resist=80
        else:
            this.afflics.stun.resist=100

    def s1_proc(this, e):
        with Modifier("s1killer", "stun_killer", "hit", 1.15):
            this.dmg_make('s1',8.48)

    def s2_proc(this, e):
        this.s2fscharge = 3

    def fs_proc(this, e):
        if this.s2fscharge > 0:
            this.s2fscharge -= 1
            this.dmg_make("o_fs_boost",0.48)
            this.afflics.stun('s2_fs', 100+this.fullhp*60, 5.5)



if __name__ == '__main__':
    #module().comment = 'boost dmg from stun 3 times'
    conf = {}
    adv_test.test(module(), conf, verbose=0)

