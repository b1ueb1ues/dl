from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Eugene

class Eugene(Adv):    
    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+Memory_of_a_Friend()
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act('c3 s end'), s
        `s3
        `s1
        `s2
        `s4, fsc and not self.inspiration()>=5 and not self.energy()>=5
        `fs, x=2
    """
    coab = ['Hunter_Sarisse', 'Dagger', 'Yurius']
    share = ['Gala_Elisanne', 'Ranzal']

    def prerun(self):
        self.phase['s1'] = 0
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff
        self.checkmate = 0
        self.s2.check = lambda: self.checkmate > 0
        self.a1_cd = False
        self.crit_mod = self.custom_crit_mod

    def custom_crit_mod(self, name):
        if self.a1_cd or name == 'test' or self.inspiration()>=5:
            return self.solid_crit_mod(name)
        else:
            crit = self.rand_crit_mod(name)
            if crit > 1 and not self.a1_cd:
                self.inspiration.add(1)
                self.a1_cd = True
                Timer(self.a1_cd_off).on(10)
            return crit

    def a1_cd_off(self, t):
        self.a1_cd = False

    @staticmethod
    def prerun_skillshare(self, dst):
        self.checkmate = 0

    def s1_proc(self, e):
        self.phase[e.name] += 1
        self.buff_class(e.name,0.20,10,'att').no_bufftime().on()
        if self.phase[e.name] == 3:
            self.buff_class(e.name,0.20,10,'crit','damage').no_bufftime().on()
            self.checkmate = min(self.checkmate+1, 2)
        self.phase[e.name] %= 3

    def s2_proc(self, e):
        self.checkmate -= 1

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)