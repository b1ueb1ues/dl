from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Fleur

class Fleur(Adv):
    comment = 'c4fs'
    a1 = ('sp',0.08,'hp70')
    a3 = ('k_paralysis',0.2)

    conf = {}
    conf['slots.a'] = TB()+SotS()
    conf['acl'] = '''
        `dragon.act('c3 s end')
        `s2, s=1
        `s1
        `s3
        `fs, seq=4
    '''
    coab = ['Blade','Sharena','Peony']
    conf['afflict_res.paralysis'] = 0

    def init(self):
        self.phase['s1'] = 0

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.phase[dst] = 0

    def s1_proc(self, e):
        with Modifier('s1killer', 'paralysis_killer', 'hit', 0.8):
            coef = 3.33
            self.dmg_make(e.name, coef)
            self.phase[e.name] += 1
            if self.phase[e.name] == 1:
                self.afflics.paralysis(e.name,110,0.883)
            else:
                self.afflics.paralysis(e.name,160, 0.883)
            self.dmg_make(e.name, coef)
            self.phase[e.name] %= 3

    def s2_proc(self, e):
        self.s1.charge(self.s1.sp)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)