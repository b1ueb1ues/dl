from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Catherine

ohoho_conf_base = {
    'x1.dmg': 0.0,
    'x1.sp': 600,
    'x1.startup': 14 / 60.0,
    'x1.recovery': 21 / 60.0,
    'x1.hit': 0,

    'x2.dmg': 0.0,
    'x2.sp': 600,
    'x2.startup': 24 / 60.0,
    'x2.recovery': 26 / 60.0,
    'x2.hit': 0,

    'x3.dmg': 0.0,
    'x3.sp': 600,
    'x3.startup': 50 / 60.0, 
    'x3.recovery': 22 / 60.0,
    'x3.hit': 0,

    'fs.dmg': 0.0,
    'fs.sp': 400,
    'fs.charge': 8 / 60.0,
    'fs.startup': 34 / 60.0,
    'fs.recovery': 36 / 60.0,
    'fs.hit': 0,
}

ohoho_conf_dmg = {
    'x1': (1.79, 2.16, 2.61, 3.13),
    'x2': (2.00, 2.40, 2.91, 3.52),
    'x3': (2.16, 2.81, 3.46, 4.11),
    'fs': (1.50, 1.80, 2.70, 3.60),
    's2': (12.42, 15.66, 17.82, 32.56),
}
ohoho_conf_hits = {
    's2': (46, 58, 66, 74)
}

class Catherine(Adv):
    a3 = ('s',0.30)

    conf = ohoho_conf_base.copy()
    conf['slots.a'] = Resounding_Rendition()+Memory_of_a_Friend()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act('c3 s end'), s
        `s3
        `s4
        `s2, self.perfect_escort=3 and self.energy()
        `s1
    """
    coab = ['Renee', 'Hunter_Sarisse', 'Summer_Estelle']
    share = ['Gala_Elisanne', 'Ranzal']

    def init(self):
        self.x_max = 3

    def prerun(self):
        self.update_perfect_escort(reset=True)

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.perfect_escort = 0
        adv.update_perfect_escort = dummy_function
    
    def s1_proc(self, e):
        self.update_perfect_escort()

    def s2_proc(self, e):
        self.update_perfect_escort(reset=True)

    def update_perfect_escort(self, reset=False):
        if reset:
            self.perfect_escort = 0
        elif self.perfect_escort < 3:
            self.perfect_escort += 1
        else:
            return
        for target, dmg in ohoho_conf_dmg.items():
            self.conf[target].dmg = dmg[self.perfect_escort]
            self.conf[target].hit = self.perfect_escort
        for target, hit in ohoho_conf_hits.items():
            self.conf[target].hit = hit[self.perfect_escort]

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
