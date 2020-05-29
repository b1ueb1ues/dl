from core.advbase import *
from slot.a import *
from module.x_alt import X_alt

def module():
    return Mitsuba

sashimi_conf = {
    # Mitsuba's Sashimi Combo
    # Total: 225
    # Total (Without Recovery): 202

    # C1: 11

    # C2A: 20
    # C2B: 20
    # C2C: 20

    # C3A: 23
    # C3B: 17
    # C3C: 25
    # C3D: 16
    # C3E: 34
    # C3F: 16
    # Recovery: 23

    # sC1 1x76%, 150SP
    # sC2 3x101%, 430SP
    # sC3 6x126%, 860SP

    # C1 A
    'x1.dmg': 76 / 100.0,
    'x1.sp': 150,
    'x1.startup': 11 / 60.0,
    'x1.recovery': 0 / 60.0,
    'x1.hit': 1,

    # C2 A B C
    'x2.dmg': 101 / 100,
    'x2.sp': 430,
    'x2.startup': 20 / 60.0,
    'x2.recovery': 0 / 60.0,
    'x2.hit': 1,

    'x3.dmg': 101 / 100,
    'x3.sp': 0,
    'x3.startup': 20 / 60.0,
    'x3.recovery': 0 / 60.0,
    'x3.hit': 1,

    'x4.dmg': 101 / 100,
    'x4.sp': 0,
    'x4.startup': 20 / 60.0,
    'x4.recovery': 0 / 60.0,
    'x4.hit': 1,

    # C3 A B C D E F
    'x5.dmg': 126 / 100,
    'x5.sp': 860,
    'x5.startup': 23 / 60.0,
    'x5.recovery': 0 / 60.0,
    'x5.hit': 1,

    'x6.dmg': 126 / 100,
    'x6.sp': 0,
    'x6.startup': 17 / 60.0,
    'x6.recovery': 0 / 60.0,
    'x6.hit': 1,

    'x7.dmg': 126 / 100,
    'x7.sp': 0,
    'x7.startup': 25 / 60.0,
    'x7.recovery': 0 / 60.0,
    'x7.hit': 1,

    'x8.dmg': 126 / 100,
    'x8.sp': 0,
    'x8.startup': 16 / 60.0,
    'x8.recovery': 0 / 60.0,
    'x8.hit': 1,

    'x9.dmg': 126 / 100,
    'x9.sp': 0,
    'x9.startup': 34 / 60.0,
    'x9.recovery': 0 / 60.0,
    'x9.hit': 1,

    'x10.dmg': 126 / 100,
    'x10.sp': 0,
    'x10.startup': 16 / 60.0,
    'x10.recovery': 23 / 60.0,
    'x10.hit': 1,
}

tempura_conf = {
    # Mitsuba's Tempura Combo:
    # Total: 302
    # Total (Without Recovery): 241

    # C1: 11

    # C2A: 16
    # C2B: 32
    # C2C: 32
    # C2D: 35

    # C3A: 42
    # C3B: 26
    # C3C: 8
    # C3D: 6
    # C3E: 20
    # C3F: 6
    # C3G: 6
    # Recovery: 61

    # tC1 1x76%, 150SP
    # tC2 4x102%, 995SP
    # tC3 7x117%, 1220SP

    # C1 A
    'x1.dmg': 76 / 100.0,
    'x1.sp': 150,
    'x1.startup': 11 / 60.0,
    'x1.recovery': 0 / 60.0,
    'x1.hit': 1,

    # C2 A B C D
    'x2.dmg': 102 / 100,
    'x2.sp': 995,
    'x2.startup': 16 / 60.0,
    'x2.recovery': 0 / 60.0,
    'x2.hit': 1,

    'x3.dmg': 102 / 100,
    'x3.sp': 0,
    'x3.startup': 32 / 60.0,
    'x3.recovery': 0 / 60.0,
    'x3.hit': 1,

    'x4.dmg': 102 / 100,
    'x4.sp': 0,
    'x4.startup': 32 / 60.0,
    'x4.recovery': 0 / 60.0,
    'x4.hit': 1,

    'x5.dmg': 102 / 100,
    'x5.sp': 0,
    'x5.startup': 35 / 60.0,
    'x5.recovery': 0 / 60.0,
    'x5.hit': 1,

    # C3 A B C D E F
    'x6.dmg': 117 / 100,
    'x6.sp': 1220,
    'x6.startup': 42 / 60.0,
    'x6.recovery': 0 / 60.0,
    'x6.hit': 1,

    'x7.dmg': 117 / 100,
    'x7.sp': 0,
    'x7.startup': 26 / 60.0,
    'x7.recovery': 0 / 60.0,
    'x7.hit': 1,

    'x8.dmg': 117 / 100,
    'x8.sp': 0,
    'x8.startup': 8 / 60.0,
    'x8.recovery': 0 / 60.0,
    'x8.hit': 1,

    'x9.dmg': 117 / 100,
    'x9.sp': 0,
    'x9.startup': 6 / 60.0,
    'x9.recovery': 0 / 60.0,
    'x9.hit': 1,

    'x10.dmg': 117 / 100,
    'x10.sp': 0,
    'x10.startup': 20 / 60.0,
    'x10.recovery': 0 / 60.0,
    'x10.hit': 1,

    'x11.dmg': 117 / 100,
    'x11.sp': 0,
    'x11.startup': 6 / 60.0,
    'x11.recovery': 0 / 60.0,
    'x11.hit': 1,

    'x12.dmg': 117 / 100,
    'x12.sp': 0,
    'x12.startup': 6 / 60.0,
    'x12.recovery': 61 / 60.0,
    'x12.hit': 1,
}

# Mitsuba's FS:
# During stances, recovery goes from 14 to 34.
# C2A FS Delay: 6
# FSF Recovery: 22
fs_conf = {
    'x2fs.charge': 14 / 60,
    'fs.recovery': 34 / 60,
    'fsf.startup': 14 / 60, # 22 - 8
}

class Mitsuba(Adv):
    a1 = ('a', 0.20, 'hit15')

    conf = fs_conf.copy()
    conf['slots.a'] = Twinfold_Bonds()+His_Clever_Brother()
    # tc2afsf tc2a- s1
    conf['acl'] = """
        if s1.check() and not self.afflics.frostbite.get()
        `sashimi
        else
        `tempura
        end
        `s1
        `s2, x=2
        `fsf, x=2
    """
    coab = ['Blade','Xander', 'Summer_Estelle']
    conf['afflict_res.frostbite'] = 0

    def prerun(self):
        self.stance = 'sashimi'
        self.next_stance = 'sashimi'
        self.stance_dict = {
            'sashimi': X_alt(self, 'sashimi', sashimi_conf, x_proc=self.l_stance_x),
            'tempura': X_alt(self, 'tempura', tempura_conf, x_proc=self.l_stance_x)
        }
        self.s1_mod = {
            'sashimi': 0.92,
            'tempura': 1.03
        }
        self.s2_buff = {
            'sashimi': (('s2', 0.10, 15, 'crit', 'chance'), 2),
            'tempura': (('s2', 0.50, 15, 'crit', 'damage'), 3)
        }

    def queue_stance(self, stance):
        # assume you can swap stance instantly instead of on next auto, to simplify acl
        if self.stance != stance and self.next_stance != stance and not self.skill._static.silence:
            log('stance', stance, 'queued')
            self.next_stance = stance
            self.update_stance()
            return True
        return False

    def update_stance(self):
        if self.hits >= 20 and self.next_stance is not None:
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

    def sashimi(self):
        return self.queue_stance('sashimi')

    def tempura(self):
        return self.queue_stance('tempura')

    def s1_proc(self, e):
        coef = self.s1_mod[self.stance]
        if self.stance == 'sashimi':
            self.hits += 1
            self.afflics.frostbite(e.name,120,0.41)
            for _ in range(7):
                self.dmg_make(e.name, coef)
                self.hits += 1
        elif self.stance == 'tempura':
            with KillerModifier('s1_killer', 'hit', 0.6, ['frostbite']):
                for _ in range(8):
                    self.dmg_make(e.name, coef)
                    self.hits += 1

    def s2_proc(self, e):
        buff, insp = self.s2_buff[self.stance]
        Teambuff(*buff).on()
        self.inspiration.add(insp, team=True)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)