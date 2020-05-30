from core.advbase import *
from slot.a import *
from slot.d import *
from module.x_alt import X_alt, Fs_alt

def module():
    return Tiki

# divine dragon mods
tiki_conf = {
    'x1.dmg': 7 / 100.0,
    'x1.sp': 88,
    'x1.utp': 2,
    'x1.startup': 12 / 60.0,
    'x1.recovery': 0,
    'x1.hit': 1,

    'x2.dmg': 15 / 100.0,
    'x2.sp': 141,
    'x2.utp': 3,
    'x2.startup': 22 / 60.0,
    'x2.recovery': 0,
    'x2.hit': 1,

    'x3.dmg': 11 / 100.0,
    'x3.sp': 178,
    'x3.utp': 4,
    'x3.startup': 36 / 60.0,
    'x3.recovery': 0 / 60.0,
    'x3.hit': 1,

    'x4.dmg': 31 / 100.0,
    'x4.sp': 350,
    'x4.utp': 5,
    'x4.startup': 26 / 60.0,
    'x4.recovery': 0 / 60.0,
    'x4.hit': 1,

    'x5.dmg': 33 / 100.0,
    'x5.sp': 367,
    'x5.utp': 6,
    'x5.startup': 20 / 60.0,
    'x5.recovery': 0 / 60.0,
    'x5.hit': 1,

    'dodge.startup': 40 / 60.0, # actually dragon dodge but w/e
}

# divine dragon mods
divine_dragon_conf = {
    'x1.dmg': 211 / 100.0,
    'x1.sp': 290,
    'x1.startup': 20 / 60.0,
    'x1.recovery': 0,
    'x1.hit': 1,

    'x2.dmg': 252 / 100.0,
    'x2.sp': 350,
    'x2.startup': 30 / 60.0,
    'x2.recovery': 0,
    'x2.hit': 1,

    'x3.dmg': 358 / 100.0,
    'x3.sp': 520,
    'x3.startup': 49 / 60.0,
    'x3.recovery': 67 / 60.0,
    'x3.hit': 1,
}

class Tiki(Adv):
    comment = 'dragon damage does not work on divine dragon'
    a1 = ('k_frostbite', 0.30)

    conf = tiki_conf.copy()
    conf['slots.a'] = Twinfold_Bonds()+The_Prince_of_Dragonyule()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['slots.d'] = Dragonyule_Jeanne()
    conf['acl'] = """
        if self.divine_dragon.get()
        `s1
        `s2
        `dodge, x=3
        else
        `dragon, self.dragonform.dragon_gauge>=1800
        `s2
        `s1
        end
    """
    coab = ['Blade', 'Xander', 'Dagger']

    def d_slots(self):
        if self.duration <= 60:
            self.conf['slots.a'] = Twinfold_Bonds()+The_Chocolatiers()
            self.conf['slots.frostbite.a'] = self.conf['slots.a']

    def x_proc(self, e):
        xseq = e.name
        utp = self.conf[xseq].utp
        self.dragonform.charge_gauge(utp, utp=True)

    def l_dragon_x(self, e):
        xalt = self.dragondrive_x
        xseq = e.name
        dmg_coef = xalt.conf[xseq].dmg
        sp = xalt.conf[xseq].sp
        hit = xalt.conf[xseq].hit
        # utp = xalt.conf[xseq].utp
        log('x', xseq, 'divine_dragon')
        self.hits += hit
        self.dmg_make(xseq, dmg_coef)
        self.charge(xseq, sp)

        # trigger updates on dgauge
        self.dragonform.charge_gauge(0, utp=True, dhaste=True)

    def prerun(self):
        self.divine_dragon = Selfbuff('divine_dragon', 1, -1, 'divine', 'dragon')
        # self.divine_dragon = Selfbuff('divine_dragon', self.dragonform.ddamage(), -1, 'att', 'dragon') # reeee
        self.dragonform.set_dragondrive(dd_buff=self.divine_dragon, max_gauge=1800, shift_cost=560, drain=40)
        Event('dragon_end').listener(self.dragondrive_on) # cursed
        Event('dragondrive_end').listener(self.dragondrive_off)

        self.dragondrive_x = X_alt(self, 'divine_dragon', divine_dragon_conf, x_proc=self.l_dragon_x, no_fs=True)

        self.o_s1 = self.s1
        self.d_s1 = Skill('s1', self.conf.s1+Conf({'startup': 0.10, 'recovery': 1.8, 'sp': 3480}))

        self.o_s2 = self.s2
        self.d_s2 = Skill('s2', self.conf.s2+Conf({'startup': 0.10, 'recovery': 1.91, 'sp': 5800}))

        self.o_s3 = self.s3
        self.d_s3 = Skill('s3', self.conf.s3+Conf({'sp': 0}))
        self.d_s3.check = lambda: False
        self.d_s3.charge = lambda sp: None

        self.o_s4 = self.s4
        self.d_s4 = Skill('s4', self.conf.s4+Conf({'sp': 0}))
        self.d_s4.check = lambda: False
        self.d_s4.charge = lambda sp: None

    def dragondrive_on(self, e):
        self.s1 = self.d_s1
        self.s2 = self.d_s2
        self.s3 = self.d_s3
        self.s4 = self.d_s4
        self.charge_p('divine_dragon', 100)
        self.dragondrive_x.on()

    def dragondrive_off(self, e):
        self.s1 = self.o_s1
        self.s2 = self.o_s2
        self.s3 = self.o_s3
        self.s4 = self.o_s4
        self.dragondrive_x.off()

    def s1_proc(self, e):
        if self.divine_dragon.get():
            self.dmg_make(e.name, 7.90)
            self.afflics.frostbite(e.name,120,0.41)
            self.dragonform.add_drive_gauge_time(self.s1.ac.getstartup()+self.s1.ac.getrecovery(), skill_pause=True)
        else:
            self.dmg_make(e.name, 3.76)
            self.dragonform.charge_gauge(260, utp=True, dhaste=True)

    def s2_proc(self, e):
        if self.divine_dragon.get():
            with KillerModifier('s2_killer', 'hit', 0.2, ['frostbite']):
                self.dmg_make(e.name, 12.05)
            self.dragonform.add_drive_gauge_time(self.s2.ac.getstartup()+self.s2.ac.getrecovery(), skill_pause=True)
        else:
            self.dragonform.charge_gauge(1000, utp=True, dhaste=True)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)