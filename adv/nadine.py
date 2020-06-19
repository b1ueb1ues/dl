from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Nadine

gyaru_phone_conf = {
    'x1.dmg': 83 / 100.0,
    'x1.sp': 190,
    'x1.startup': 24 / 60.0,
    'x1.recovery': 18 / 60.0,
    'x1.hit': 1,

    'x2.dmg': 83 / 100.0,
    'x2.sp': 190,
    'x2.startup': 12 / 60.0,
    'x2.recovery': 12 / 60.0,
    'x2.hit': 1,

    'x3.dmg': 111 / 100.0,
    'x3.sp': 255,
    'x3.startup': 14 / 60.0, 
    'x3.recovery': 10 / 60.0,
    'x3.hit': 1,

    'x4.dmg': 111 / 100.0,
    'x4.sp': 255,
    'x4.startup': 12 / 60.0,
    'x4.recovery': 12 / 60.0,
    'x4.hit': 1,

    'x5.dmg': 167 / 100.0,
    'x5.sp': 400,
    'x5.startup': 16 / 60.0,
    'x5.recovery': 42 / 60.0,
    'x5.hit': 1,

    'fs.dmg': 150 / 100.0,
    'fs.sp': 400,
    'fs.charge': 9 / 60.0,
    'fs.startup': 22 / 60.0,
    'fs.recovery': 38 / 60.0,
    'fs.hit': 1,
}

class Nadine(Adv):
    a1 = ('eextra_rng', 1)
    a3 = ('energized_att', 0.20)

    conf = gyaru_phone_conf.copy()
    conf['slots.a'] = Resounding_Rendition()+Me_and_My_Bestie()
    conf['acl'] = """
        `dragon.act('c1 s s end'), s=1
        `s3, not self.s3_buff
        `s2
        `s1
        `fs, x=5
        """
    coab = ['Blade', 'Wand', 'Marth']
    conf['afflict_res.burn'] = 0

    def prerun(self):
        self.team_s1_hits = 1
        teammates = 2
        if self.condition(f'{teammates} teammates in s1'):
            self.team_s1_hits += teammates
        self.s2_ss = Selfbuff('s2_ss', 1, 15, 'upgrade', 's1')

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.team_s1_hits = 1
        teammates = 2
        if adv.condition(f'{teammates} teammates in s1'):
            adv.team_s1_hits += teammates
        adv.s2_ss = Dummy()

    def s1_proc(self, e):
        is_ss = self.s2_ss.get()
        s1_hits = self.team_s1_hits + 1
        if is_ss:
            s1_hits += 2
        self.dmg_make(e.name, 8.22)
        self.hits += s1_hits
        self.afflics.burn(e.name,120,0.97)
        if s1_hits == 3:
            self.dmg_make(e.name, 1.64)
            self.energy.add(1)
        elif s1_hits == 4 or s1_hits == 5:
            self.dmg_make(e.name, 3.29)
            self.energy.add(3)
        elif s1_hits > 5:
            self.dmg_make(e.name, 5.75)
            self.energy.add(5)
        self.hits += 1

    def s2_proc(self, e):
        if random.random() < 0.50:
            self.s2_ss.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)