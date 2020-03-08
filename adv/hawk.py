import adv.adv_test
from core.advbase import *
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
    conf['afflict_res.stun'] = 80
    def init(self):
        self.s2fscharge = 0
        if self.condition('hp100'):
            self.fullhp = 1
        else:
            self.fullhp = 0

    def s1_proc(self, e):
        with Modifier("s1killer", "stun_killer", "hit", 1.15):
            self.dmg_make('s1',8.48)

    def s2_proc(self, e):
        self.s2fscharge = 3

    def fs_proc(self, e):
        if self.s2fscharge > 0:
            self.s2fscharge -= 1
            self.dmg_make("o_fs_boost",0.48)
            self.afflics.stun('s2_fs', 100+self.fullhp*60, 5.5)



if __name__ == '__main__':
    #module().comment = 'boost dmg from stun 3 times'
    conf = {}
    adv.adv_test.test(module(), conf)

