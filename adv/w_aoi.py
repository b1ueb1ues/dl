from core.advbase import *
from slot.a import *

def module():
    return Wedding_Aoi

class Wedding_Aoi(Adv):
    a1 = ('affteam_sleep', 0.15, 10, 5)
    a3 = ('sp',0.12,'fs')
    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+Primal_Crisis()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `fs, seq=5
        """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']
    conf['afflict_res.sleep'] = 80

    def init(self):
        if self.condition('big hitbox'):
            self.s1_addition = 4
        else:
            self.s1_addition = 1

    def s1_before(self, e):
        self.dmg_make('o_s1_hit1',1.47)
        self.afflics.sleep('s1',110,6.5)

    def s1_proc(self, e):
        if self.s1_addition == 4:
            self.dmg_make('o_s1_hit2',1.47)
            self.dmg_make('o_s1_hit3',1.47)
            self.dmg_make('o_s1_hit4',1.47)
        elif self.s1_addition == 1:
            pass

    def s2_proc(self, e):
        with Modifier("s1killer", "sleep_killer", "hit", 1):
            self.dmg_make('s1',5*1.40)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)