from core.advbase import *
from slot.a import *

def module():
    return Joachim

class Joachim(Adv):
    comment = ''
    a1 = ('a',0.10,'hp70')
    a3 = ('k_poison',0.2)
    
    conf = {}
    conf['slots.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s2, s=1
        `s1
    """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']
    conf['afflict_res.poison'] = 0

    def init(self):
        self.s1_stance = 1

    def s1_proc(self, e):
        with Modifier("s1killer", "poison_killer", "hit", 0.8):
            coef = 2.2
            self.dmg_make('s1', coef)

            if self.s1_stance == 1:
                self.afflics.poison('s1',110, 0.53)
                self.s1_stance = 2
            elif self.s1_stance == 2:
                self.afflics.poison('s1',160, 0.53)
                self.s1_stance = 3
            elif self.s1_stance == 3:
                Teambuff("s1atk",0.15,10).on()
                self.afflics.poison('s1',160, 0.53)
                self.s1_stance = 1

            self.dmg_make('s1', coef)


    def s2_proc(self, e):
        self.s1.charge(self.s1.sp)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)