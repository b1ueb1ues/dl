from core.advbase import *
from slot.a import *
from slot.d import *
from module.x_alt import X_alt

def module():
    return Tobias

# C1: 1x 73% Damage + 80 SP
# C2: 2x 82% Damage + 80 SP
# C3: 2x 88% Damage + 138 SP
# C4: 2x 90% Damage + 226 SP
# C5: 2x 97% Damage + 415 SP

# s2,88,,
# s2,190,102,1.7
# x1,210,20,0.333333333
# x2,223,13,0.216666667
# x2,237,14,0.233333333
# x3,253,16,0.266666667
# x3,267,14,0.233333333
# x4,283,16,0.266666667
# x4,298,15,0.25
# x5,314,16,0.266666667
# x5,328,14,0.233333333
# x1,359,31,0.516666667
# x2,374,15,0.25
# x2,388,14,0.233333333
# x3,404,16,0.266666667
# x3,418,14,0.233333333
# x4,435,17,0.283333333
# x4,449,14,0.233333333
# x5,464,15,0.25
# x5,479,15,0.25
# x1,509,30,0.5


sacred_blade_conf = {
    'x1.dmg': 73 / 100.0,
    'x1.sp': 80,
    'x1.startup': 20 / 60.0,
    'x1.recovery': 30 / 60.0,
    'x1.hit': 1,

    'x2.dmg': 164 / 100.0,
    'x2.sp': 80,
    'x2.startup': 0,
    'x2.recovery': 30 / 60.0,
    'x2.hit': 2,

    'x3.dmg': 176 / 100.0,
    'x3.sp': 138,
    'x3.startup': 0,
    'x3.recovery': 30 / 60.0,
    'x3.hit': 2,

    'x4.dmg': 180 / 100.0,
    'x4.sp': 226,
    'x4.startup': 0,
    'x4.recovery': 30 / 60.0,
    'x4.hit': 2,

    'x5.dmg': 194 / 100.0,
    'x5.sp': 415,
    'x5.startup': 0,
    'x5.recovery': 10 / 60.0,
    'x5.hit': 2,
}


class Tobias(Adv):
    a1 = ('bt',0.25)
    a3 = ('k_poison',0.3)

    conf = {}
    conf['slots.a'] = A_Dogs_Day()+Castle_Cheer_Corps()
    conf['slots.poison.a'] = conf['slots.a']
    conf['slots.d'] = Freyja()
    conf['acl'] = """
        `s4
        `s1
        `s3
    """
    coab = ['Bow','Blade','Tiki']
    share = ['Patia','Summer_Luca']

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.buff_class = Dummy if adv.slots.c.ele != 'wind' else Teambuff if adv.condition('buff all team') else Selfbuff

    def prerun(self):
        self.s2_mode = 0
        self.s1.autocharge_init(85)
        self.s2.charge(1)
        self.s2_x_alt = X_alt(self, 'sacred_blade', sacred_blade_conf, x_proc=self.l_sacred_blade_x, no_fs=True, no_dodge=True)
        self.a_s2 = self.s2.ac
        self.a_s2a = S('s2', Conf({'startup': 0.10, 'recovery': 1.91}))

    def l_sacred_blade_x(self, e):
        xseq = e.name
        dmg_coef = self.s2_x_alt.conf[xseq].dmg
        sp = self.s2_x_alt.conf[xseq].sp
        hit = self.s2_x_alt.conf[xseq].hit
        log('x', xseq, 'sacred_blade')
        self.hits += hit
        self.dmg_make(xseq, dmg_coef)
        self.charge(xseq, sp)

    def s1_autocharge_off(self, t):
        self.s1.autocharge_timer.off()

    def s2_x_alt_off(self, t):
        self.s2_mode = 0
        self.s2.ac = self.a_s2
        self.s2.charged = 0
        self.s2_x_alt.off()

    def s1_proc(self, e):
        self.buff_class(e.name,0.3,15).on()

    def s2_proc(self, e):
        if self.s2_mode == 0:
            self.s2.ac = self.a_s2a
            self.s2_x_alt.on()
            self.s1.autocharge_timer.on()
            Timer(self.s1_autocharge_off).on(7*self.mod('buff'))
            Timer(self.s2_x_alt_off).on(10*self.mod('buff'))
        else:
            self.dmg_make(e.name,1.04)
            self.hits += 8
            self.afflics.poison(e.name, 120, 0.582)
            self.s2.ac = self.a_s2
            self.s2_x_alt.on()
            self.s1.autocharge_timer.off()
        self.s2.charge(1)
        self.s2_mode = (self.s2_mode + 1) % 2


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)