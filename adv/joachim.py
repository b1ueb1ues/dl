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
    conf['acl'] = '''
        `dragon.act('c3 s end')
        `s3, not self.s3_buff
        `s2, s=1
        `s1
    '''
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']
    conf['afflict_res.poison'] = 0

    def init(self):
        self.phase['s1'] = 0

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.phase[dst] = 0

    def s1_proc(self, e):
        with KillerModifier('s1_killer', 'hit', 0.8, ['poison']):
            coef = 2.2
            self.dmg_make(e.name, coef)

            self.phase[e.name] += 1
            if self.phase[e.name] == 1:
                self.afflics.poison(e.name,110, 0.53)
            elif self.phase[e.name] == 2:
                self.afflics.poison(e.name,160, 0.53)
            elif self.phase[e.name] == 3:
                Teambuff(e.name,0.15,10).on()
                self.afflics.poison(e.name,160, 0.53)
            self.phase[e.name] %= 3

            self.dmg_make(e.name, coef)


    def s2_proc(self, e):
        self.s1.charge(self.s1.sp)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)