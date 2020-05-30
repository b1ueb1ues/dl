from core.advbase import *
from slot.d import *
from slot.a import *
from module.x_alt import X_alt

def module():
    return Gala_Leif

striking_conf = {
    'x1.dmg': 112 / 100.0,
    'x1.sp': 152,
    'x1.startup': 10 / 60.0,
    'x1.recovery': 0 / 60.0,
    'x1.hit': 2,

    'x2.dmg': 174 / 100.0,
    'x2.sp': 345,
    'x2.startup': 44 / 60.0,
    'x2.recovery': 0 / 60.0,
    'x2.hit': 3,

    'x3.dmg': 327 / 100.0,
    'x3.sp': 655,
    'x3.startup': 40 / 60.0,
    'x3.recovery': 30 / 60.0, # needs verification
    'x3.hit': 5,
}

shielding_conf = {
    'x1.dmg': 182 / 100.0,
    'x1.sp': 400,
    'x1.startup': 16 / 60.0,
    'x1.recovery': 0 / 60.0,
    'x1.hit': 1,

    'x2.dmg': 367 / 100.0,
    'x2.sp': 600,
    'x2.startup': 56 / 60.0,
    'x2.recovery': 0 / 60.0,
    'x2.hit': 1,

    'x3.dmg': 548 / 100.0,
    'x3.sp': 800,
    'x3.startup': 76 / 60.0,
    'x3.recovery': 30 / 60.0, # needs verification
    'x3.hit': 1,
}

class Gala_Leif(Adv):
    a1 = ('dbt', 0.20)
    a3 = ('a', 0.20, 'hit15')

    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+The_Fires_of_Hate()
    conf['slots.d'] = Vayu()
    conf['acl'] = """
        if s1.check()
        `striking
        elif s2.check()
        `shielding
        end
        `dragon.act('c3 s end')
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, x=3
    """
    coab = ['Dragonyule_Xainfried', 'Blade', 'Lin_You']
    
    def prerun(self):
        self.stance = 'shielding'
        self.next_stance = 'shielding'
        self.stance_dict = {
            'striking': X_alt(self, 'striking', striking_conf, x_proc=self.l_stance_x),
            'shielding': X_alt(self, 'shielding', shielding_conf, x_proc=self.l_stance_x)
        }
        self.stance_ac_dict = {
            'striking': (self.s1.ac, self.s2.ac),
            'shielding': (
                S('s1', Conf({'startup': 0.10, 'recovery': 1.30})),
                S('s2', Conf({'startup': 0.10, 'recovery': 3.00}))
            )
        }
        self.s1_defdown = Debuff('s1', 0.05, 20, 1)
        self.s2_attdown = Debuff('s2', 0.05, 20, 1, 'attack')

    def s1_proc(self, e):
        if self.stance == 'striking':
            self.dmg_make(e.name, 4.29)
            self.s1_defdown.on()
            self.dmg_make(e.name, 4.50)
        else:
            Selfbuff(e.name, 0.60, 15, 'defense').on()

    def s2_proc(self, e):
        if self.stance == 'striking':
            with KillerModifier('s2_killer', 'hit', 0.2, ['poison']):
                self.dmg_make(e.name, 4.91)
                self.s2_attdown.on()
                self.dmg_make(e.name, 4.91+5.40)
                self.hits += 3
        else:
            with KillerModifier('s2_killer', 'hit', 0.2, ['debuff_def']):
                self.dmg_make(e.name, 7.02)
                self.afflics.poison(e.name, 120, 0.582)
                self.dmg_make(e.name, 7.72+8.42)
                self.hits += 3

    def queue_stance(self, stance):
        # assume you can swap stance instantly instead of on next auto, to simplify acl
        if self.stance != stance and self.next_stance != stance:
            log('stance', stance, 'queued')
            self.next_stance = stance
            self.update_stance()
            return True
        return False

    def update_stance(self):
        if self.hits >= 5 and self.next_stance is not None and not self.skill._static.silence:
            curr_stance = self.stance_dict[self.stance]
            curr_stance.off()
            next_stance = self.stance_dict[self.next_stance]
            self.s1.ac, self.s2.ac = self.stance_ac_dict[self.next_stance]
            next_stance.on()
            self.stance = self.next_stance
            self.next_stance = None

    def x_proc(self, e):
        self.update_stance()

    def l_stance_x(self, e):
        xalt = self.stance_dict[self.stance]
        xseq = e.name
        dmg_coef = xalt.conf[xseq].dmg
        sp = xalt.conf[xseq].sp
        hit = xalt.conf[xseq].hit
        log('x', xseq, self.stance)
        self.hits += hit
        self.dmg_make(xseq, dmg_coef)
        self.charge(xseq, sp)
        self.update_stance()

    def striking(self):
        return self.queue_stance('striking')

    def shielding(self):
        return self.queue_stance('shielding')


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)