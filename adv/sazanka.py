import adv.adv_test
from core.advbase import *
from module.bleed import Bleed
from slot.d import *
from slot.a import *

def module():
    return Sazanka

class Sazanka(Adv):
    a3 = ('k_sleep', 0.20)

    conf = {}
    conf['slot.d'] = Shinobi()
    conf['slot.a'] = KFM()+CE()
    conf['acl'] = """
        `s1
        `s3, fsc
        `s2, fsc
        `fs, seq=5
        """
    conf['afflict_res.sleep'] = 80

    def prerun(self):
        self.bleed = Bleed("g_bleed",0).reset()
        self.s2fscharge = 0

    def s1_proc(self, e):
        if random.random() < 0.8:
            Bleed("s1", 1.32).on()

    def s2_proc(self, e):
        self.s2fscharge = 3

    def fs_proc(self, e):
        if self.s2fscharge > 0:
            self.s2fscharge -= 1
            self.dmg_make("o_fs_boost",0.38)
            self.afflics.sleep('s2_fs', 100, 4.5)



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
