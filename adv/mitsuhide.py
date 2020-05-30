from core.advbase import *
from slot.a import *

def module():
    return Mitsuhide

class Mitsuhide(Adv):
    a1 = ('a',0.2,'hit15')
    a3 = ('k_paralysis',0.3)

    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon
        `s1
        `s2
        `s3
        `fs, seq=4
    """
    coab = ['Blade','Sharena','Peony']
    conf['afflict_res.paralysis'] = 0

    def init(self):
        self.s1_stance = 1

    def s1_proc(self, e):
        self.dmg_make(e.name,0.61)
        self.afflics.paralysis(e.name,120, 0.97)
        for _ in range(11):
            self.dmg_make(e.name,0.61)
            self.hits += 1

    def s2_proc(self, e):
        if(self.hits >= 5):
            self.dmg_make(e.name,0.4725)
        if(self.hits >= 10):
            self.dmg_make(e.name,0.4725)
        if(self.hits >= 15):
            self.dmg_make(e.name,0.945)
        if(self.hits >= 20):
            self.dmg_make(e.name,0.945)
        if(self.hits >= 25):
            self.dmg_make(e.name,0.945)
        if(self.hits >= 30):
            self.dmg_make(e.name,0.945)

        Spdbuff(e.name,0.1,10).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)