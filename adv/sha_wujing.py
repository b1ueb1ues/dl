from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Sha_Wujing

class Sha_Wujing(Adv):
    conf = {}
    conf['slots.a'] = Dragon_and_Tamer()+Primal_Crisis()
    conf['slots.paralysis.a'] = Resounding_Rendition()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon, s=2
        `s2, cancel
        `s1
        `fs, x=5
    """
    coab = ['Blade','Dagger','Peony']

    def prerun(self):
        self.s1_p = 0
        self.s1_defdown = Debuff('s1', 0.05, 10, 1)
        self.s1_mods = [
            (3.37, 3.53),
            (3.87, 3.70),
            (4.04, 4.21)
        ]
        self.a1_count = 3
        Timer(self.a3_start).on(self.duration*0.3)

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.a1_check = lambda: False

    def a3_start(self, t):
        Selfbuff('a3', 0.08, -1, 'att', 'assailant').on()

    def a1_check(self):
        if self.a1_count > 0:
            self.a1_count -= 1
            Selfbuff('a1', 0.06, -1, 's', 'buff').on()

    def s1_proc(self, e):
        hit1, hit2 = self.s1_mods[self.s1_p]
        self.s1_p += 1
        self.dmg_make(e.name, hit1)
        self.hits += 1
        if self.s1_p > 1:
            self.s1_defdown.on()
        if self.s1_p > 2:
            self.charge_p(e.name, 0.30, target='s2')
        self.dmg_make(e.name, hit2)
        self.hits += 1
        self.s1_p %= 3

        self.a1_check()

    def s2_proc(self, e):
        if self.condition(f'{e.name} defdown for 10s'):
            self.s2_debuff = Debuff(e.name,0.15,10,1)
            self.s2_debuff.bufftime = self.s2_debuff._no_bufftime
            self.s2_debuff.on()
        
        self.a1_check()

    def s3_proc(self, e):
        self.a1_check()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)