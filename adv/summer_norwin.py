from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Summer_Norwin

class Summer_Norwin(Adv):
    a1 = ('ehaste', 3)
    a3 = ('k_poison',0.30)
    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+The_Plaguebringer()
    conf['slots.poison.a'] = conf['slots.a']
    conf['acl'] = """
        `dragon.act("c3 s end"), x=5 and s1.charged<2000
        `s3, not self.s3_buff
        `s1
        `s2, x=5
        `s4, x=5
        """
    coab = ['Blade','Dragonyule_Xainfried','Eleonora']
    share = ['Curran']

    def prerun(self):
        self.phase_s12 = 0
        self.doleful = 0

    @staticmethod
    def prerun_skillshare(adv, dst):
        self.phase_s12 = -1

    def s1_proc(self, e):
        if self.phase_s12 == -1:
            self.energy.add(5, team=True)
            return
        self.phase_s12 += 1
        if self.phase_s12 == 1:
            self.dmg_make(f'{e.name}_p{self.phase_s12}', 12.60)
        elif self.phase_s12 == 2:
            self.dmg_make(f'{e.name}_p{self.phase_s12}', 13.86)
        elif self.phase_s12 == 3:
            self.dmg_make(f'{e.name}_p{self.phase_s12}', 16.38)
        elif self.phase_s12 == 4:
            self.doleful = 0
            self.energy.disabled = False
            self.energy.add(5, team=True)
        self.phase_s12 %= 4

    def s2_proc(self, e):
        self.phase_s12 += 1
        if self.phase_s12 == 1:
            self.dmg_make(f'{e.name}_p{self.phase_s12}', 12.60)
        elif self.phase_s12 == 2:
            self.dmg_make(f'{e.name}_p{self.phase_s12}', 13.86)
        elif self.phase_s12 == 3:
            self.dmg_make(f'{e.name}_p{self.phase_s12}', 16.38)
        elif self.phase_s12 == 4:
            self.set_hp(self.hp*(1-self.doleful*0.20))
            self.dmg_make(f'{e.name}_p{self.phase_s12}', 20.16)
            self.afflics.poison(f'{e.name}_p{self.phase_s12}',120,0.582,30)
            self.doleful = min(self.doleful+1, 4)
            self.energy.disabled = True
        self.phase_s12 %= 4


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
