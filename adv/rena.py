from core.advbase import *
from slot.a import *

def module():
    return Rena

class Rena(Adv):
    a1 = ('primed_defense',0.08)

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Elegant_Escort()
    conf['acl'] = """
        `dragon, s=1
        `s3, not self.s3_buff
        `s1
        `s2, s=1
        `fs, x=5 and (s1.charged=1500 or s1.charged=3200)
    """
    coab = ['Wand', 'Joe', 'Marth']    
    conf['afflict_res.burn'] = 0

    def d_coabs(self):
        if self.duration <= 120:
            self.coab = ['Blade','Wand','Serena']

    def prerun(self):
        self.phase['s1'] = 0

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.phase[dst] = 0

    def s1_proc(self, e):
        self.phase[e.name] += 1
        if self.phase[e.name] == 1:
            self.dmg_make(e.name, 0.72)
            self.hits += 1
            self.afflics.burn(e.name,120,0.97)
            self.dmg_make(e.name,8.81)
            self.hits += 4
        elif self.phase[e.name] == 2:
            self.dmg_make(e.name, 0.72)
            self.afflics.burn(e.name,120,0.97)
            self.hits += 1
            self.dmg_make(e.name,8.81)
            Selfbuff(e.name,0.1,15,'crit','chance').on()
            self.hits += 4
        elif self.phase[e.name] == 3:
            with KillerModifier('s1_killer', 'hit', 0.8, ['burn']):
                self.dmg_make(e.name, 0.72)
                self.hits += 1
                self.afflics.burn(e.name,120,0.97)
                self.dmg_make(e.name, 8.81)
                self.hits += 4
            Selfbuff(e.name,0.1,15,'crit','chance').on()
        self.phase[e.name] %= 3

    def s2_proc(self, e):
        self.s1.charge(self.s1.sp)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
