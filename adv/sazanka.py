from core.advbase import *
from module.bleed import Bleed
from slot.d import *
from slot.a import *

def module():
    return Sazanka

class Sazanka(Adv):
    a3 = ('k_sleep', 0.20)

    conf = {}
    conf['slots.a'] = KFM()+Crystalian_Envoy()
    conf['slots.d'] = Shinobi()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2, fsc
        `fs, seq=5
    """
    coab = ['Blade','Wand','Dagger']
    conf['afflict_res.sleep'] = 80

    def prerun(self):
        self.bleed = Bleed('g_bleed',0).reset()
        self.s2fscharge = 0

    def s1_proc(self, e):
        if random.random() < 0.8:
            Bleed(e.name, 1.32).on()

    def s2_proc(self, e):
        self.s2fscharge = 3

    def fs_proc(self, e):
        if self.s2fscharge > 0:
            self.s2fscharge -= 1
            self.dmg_make(f'{e.name}_boost',0.38)
            self.afflics.sleep(f'{e.name}_fs', 100, 4.5)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
