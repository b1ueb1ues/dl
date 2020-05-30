from core.advbase import *
from slot.a import *
from slot.d import *
from module.x_alt import X_alt
import random

def module():
    return Valerio


dessert_conf = {
    # Valerio's Dessert Combo:
    # Total: 274
    # Total (No Recovery): 205
    # C1: 29
    # C2A: 86
    # C2B: 16
    # C2C: 8
    # C2D: 4
    # C3: 62
    # Recovey: 69

    # Dessert Stance
    # mC1 1 hit 195% 350SP (1.041s startup to cancel into mC2)
    # mC2 4 hits 27% 710SP (uses same Absorb effect as Axe C4, 1.73333s to cancel into mC3)
    # mc3 1 hit 453% 1590SP (cancelled @1.1573s)

    # C1 A
    'x1.dmg': 195 / 100.0,
    'x1.sp': 350,
    'x1.startup': 29 / 60.0,
    'x1.recovery': 0 / 60.0,
    'x1.hit': 1,

    # C2 A B C D
    'x2.dmg': 27 / 100.0,
    'x2.sp': 710,
    'x2.startup': 86 / 60.0,
    'x2.recovery': 0 / 60.0,
    'x2.hit': 1,

    'x3.dmg': 27 / 100.0,
    'x3.sp': 0,
    'x3.startup': 16 / 60.0,
    'x3.recovery': 0 / 60.0,
    'x3.hit': 1,

    'x4.dmg': 27 / 100.0,
    'x4.sp': 0,
    'x4.startup': 8 / 60.0,
    'x4.recovery': 0 / 60.0,
    'x4.hit': 1,

    'x5.dmg': 27 / 100.0,
    'x5.sp': 0,
    'x5.startup': 4 / 60.0,
    'x5.recovery': 0 / 60.0,
    'x5.hit': 1,

    # C3 A
    'x6.dmg': 453 / 100.0,
    'x6.sp': 1590,
    'x6.startup': 62 / 60.0,
    'x6.recovery': 69 / 60.0,
    'x6.hit': 1,
}

entree_conf = {
    # Valerio's Entree Combo:
    # Total: 269
    # Total (No Recovery): 203
    # C1: 29
    # C2A: 66
    # C2B: 15
    # C2C: 22
    # C3A: 57 (x4 hits)
    # C3B: 8 (x4 hits)
    # C3C: 6 (x4 hits)
    # Recovery (from C3C hit, I'm not sure if C3 is a projectile as a whole or not): 66

    # Entree Stance
    # mC1 1 hit 195% 350SP  (1.041s startup to cancel into mC2)
    # mC2 3 hits 162% 700SP  (1.0185s startup to cancel into mC3)
    # mc3 12 bullets 38% 720SP Attenuation rate 1.0 hitinterval 0.5, 0 Additional collisions (signaldata sent @1.6s forced cancel @2s)

    # C1 A
    'x1.dmg': 195 / 100.0,
    'x1.sp': 350,
    'x1.startup': 29 / 60.0,
    'x1.recovery': 0 / 60.0,
    'x1.hit': 1,

    # C2 A B C
    'x2.dmg': 162 / 100.0,
    'x2.sp': 700,
    'x2.startup': 66 / 60.0,
    'x2.recovery': 0 / 60.0,
    'x2.hit': 1,

    'x3.dmg': 162 / 100.0,
    'x3.sp': 0,
    'x3.startup': 15 / 60.0,
    'x3.recovery': 0 / 60.0,
    'x3.hit': 1,

    'x4.dmg': 162 / 100.0,
    'x4.sp': 0,
    'x4.startup': 22 / 60.0,
    'x4.recovery': 0 / 60.0,
    'x4.hit': 1,

    # C3 A B C
    'x5.dmg': 152 / 100.0,
    'x5.sp': 720,
    'x5.startup': 57 / 60.0,
    'x5.recovery': 0 / 60.0,
    'x5.hit': 4,

    'x6.dmg': 152 / 100.0,
    'x6.sp': 0,
    'x6.startup': 8 / 60.0,
    'x6.recovery': 0 / 60.0,
    'x6.hit': 4,

    'x7.dmg': 152 / 100.0,
    'x7.sp': 0,
    'x7.startup': 6 / 60.0,
    'x7.recovery': 66 / 60.0,
    'x7.hit': 4,
}

appetizer_conf = {
    # Valerio's Appetizer Combo:
    # C1: 29
    # C2A: 56 (x2 hits) (High Damage)
    # C2B: 6 (x4 hits) (Two High Damage, Two Low)
    # C2C: 6 (x4 hits) (Low Damage)
    # C2D: 24 (x4 hits) (Low Damage)
    # C2E: 6 (x4 hits) (Low Damage)
    # C2F: 6 (x4 hits) (Low Damage)
    # C3A: 46
    # C3B: 99
    # C3C: 4
    # C3D: 4
    # Recovery (from C3D, idk if C3 is a projectile or not): 9

    # Appetiser stance
    # mC1 1 hit 195% 350SP (1.041s statup to cancel into mC2)
    # mC2 4 hit 129%  + 18 bullets 6% 680SP (1.0256s startup to cancel into mC3)
    # mC3 1 hit 143% (@0.4s) + 1 hit 143% (@2.067s) + 1 hit 143% (@2.13s) + 1 hit 143% (@2.2s) can end mC3 any time between 0.433333s and 2.067s by doing ANYTHING  1030SP (forced cancel at 2.267s)

    # C1 A
    'x1.dmg': 195 / 100.0,
    'x1.sp': 350,
    'x1.startup': 29 / 60.0,
    'x1.recovery': 0 / 60.0,
    'x1.hit': 1,

    # C2 A B CDEF
    'x2.dmg': 258 / 100.0,
    'x2.sp': 680,
    'x2.startup': 56 / 60.0,
    'x2.recovery': 0 / 60.0,
    'x2.hit': 2,

    'x3.dmg': (258+12) / 100.0,
    'x3.sp': 0,
    'x3.startup': 6 / 60.0,
    'x3.recovery': 0 / 60.0,
    'x3.hit': 4,

    'x4.dmg': 24 / 100.0,
    'x4.sp': 0,
    'x4.startup': 6 / 60.0,
    'x4.recovery': 0 / 60.0,
    'x4.hit': 4,

    'x5.dmg': 24 / 100.0,
    'x5.sp': 0,
    'x5.startup': 24 / 60.0,
    'x5.recovery': 0 / 60.0,
    'x5.hit': 4,

    'x6.dmg': 24 / 100.0,
    'x6.sp': 0,
    'x6.startup': 6 / 60.0,
    'x6.recovery': 0 / 60.0,
    'x6.hit': 4,

    'x7.dmg': 24 / 100.0,
    'x7.sp': 0,
    'x7.startup': 6 / 60.0,
    'x7.recovery': 0 / 60.0,
    'x7.hit': 4,

    # C3 A B C D
    'x8.dmg': 143 / 100.0,
    'x8.sp': 1030,
    'x8.startup': 46 / 60.0,
    'x8.recovery': 0 / 60.0,
    'x8.hit': 1,

    'x9.dmg': 143 / 100.0,
    'x9.sp': 0,
    'x9.startup': 99 / 60.0,
    'x9.recovery': 0 / 60.0,
    'x9.hit': 1,

    'x10.dmg': 143 / 100.0,
    'x10.sp': 0,
    'x10.startup': 4 / 60.0,
    'x10.recovery': 0 / 60.0,
    'x10.hit': 1,

    'x11.dmg': 143 / 100.0,
    'x11.sp': 0,
    'x11.startup': 4 / 60.0,
    'x11.recovery': 9 / 60.0,
    'x11.hit': 1,
}


class Valerio(Adv):
    conf = {}
    conf['slots.a'] = The_Wyrmclan_Duo()+Primal_Crisis()
    conf['slots.frostbite.a'] = Primal_Crisis()+His_Clever_Brother()
    conf['slots.d'] = Siren()
    conf['acl'] = """
        # stances
        if s1.check() and self.s1_debuff.buff_end_timer.timing-now()<7
        `appetizer
        elif s2.check() and self.inspiration()=0
        `entree
        else
        `dessert
        end
        # actions
        `s2
        `s1
        `s3
    """
    coab = ['Summer_Estelle', 'Renee', 'Xander']
    conf['afflict_res.frostbite'] = 0

    def prerun(self):
        random.seed()
        self.stance = 'dessert'
        self.next_stance = 'dessert'
        self.stance_dict = {
            'appetizer': X_alt(self, 'appetizer', appetizer_conf, x_proc=self.l_stance_x),
            'entree': X_alt(self, 'entree', entree_conf, x_proc=self.l_stance_x),
            'dessert': X_alt(self, 'dessert', dessert_conf, x_proc=self.l_stance_x),
        }
        self.crit_mod = self.custom_crit_mod
        self.a1_cd = False
        self.s1_debuff = Debuff('s1', 0.05, 30)
        self.s1_mod = {
            'appetizer': 1.29,
            'entree': 1.77,
            'dessert': 1.77
        }
        self.s2_buff = {
            'appetizer': (Teambuff('s2', 0.08, 15, 'defense'), 2),
            'entree': (Teambuff('s2', 0.10, 15, 'crit', 'chance'), 3),
            'dessert': (Teambuff('s2', 0.08, 15), 2)
        }

    def custom_crit_mod(self, name):
        if self.a1_cd or name == 'test':
            return self.solid_crit_mod(name)
        else:
            crit = self.rand_crit_mod(name)
            if crit > 1 and not self.a1_cd:
                Spdbuff('a1', 0.10, 20).on()
                self.a1_cd = True
                Timer(self.a1_cd_off).on(10)
            return crit

    def a1_cd_off(self, t):
        self.a1_cd = False

    def queue_stance(self, stance):
        # assume you can swap stance instantly instead of on next auto, to simplify acl
        if self.stance != stance and self.next_stance != stance:
            log('stance', stance, 'queued')
            self.next_stance = stance
            self.update_stance()
            return True
        return False

    def update_stance(self):
        if self.hits >= 20 and self.next_stance is not None and not self.skill._static.silence:
            curr_stance = self.stance_dict[self.stance]
            curr_stance.off()
            next_stance = self.stance_dict[self.next_stance]
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

    def appetizer(self):
        return self.queue_stance('appetizer')

    def entree(self):
        return self.queue_stance('entree')

    def dessert(self):
        return self.queue_stance('dessert')

    def s1_proc(self, e):
        self.dmg_make(e.name, self.s1_mod[self.stance])
        self.hits += 1
        if self.stance == 'appetizer':
            self.afflics.frostbite(e.name,120,0.41)
            self.s1_debuff.on()
        for _ in range(5):
            self.dmg_make(e.name, self.s1_mod[self.stance])
            self.hits += 1

    def s2_proc(self, e):
        buff, insp = self.s2_buff[self.stance]
        buff.on()
        self.inspiration.add(insp, team=True)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)