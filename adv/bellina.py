from core.advbase import *
from slot.a import *
from slot.d import *
from module.x_alt import X_alt, Fs_alt

def module():
    return Bellina

# 2x crisis mods on autos and fs
dragondrive_auto_conf = {
    'x1.dmg': 189 / 100.0,
    'x1.sp': 290,
    'x1.utp': 180,
    'x1.startup': 27 / 60.0,
    'x1.recovery': 0,
    'x1.hit': 1,

    'x2.dmg': 227 / 100.0,
    'x2.sp': 350,
    'x2.utp': 180,
    'x2.startup': 35 / 60.0,
    'x2.recovery': 0,
    'x2.hit': 1,

    'x3.dmg': 340 / 100.0,
    'x3.sp': 520,
    'x3.utp': 240,
    'x3.startup': 40 / 60.0,
    'x3.recovery': 40 / 60.0,
    'x3.hit': 1,
}

dragondrive_fs_conf = {
    'fs.dmg': 0 / 100.0,
    'fs.sp': 360,
    'fs.utp': 900,
    'fs.charge': 120 / 60.0,
    'fs.startup': 4 / 60.0,
    'fs.recovery': 31 / 60.0,
    'fs.hit': -1,

    'x1fs.charge': 120 / 60.0,
    'fsf.charge': 5 / 60.0,
    'fsf.startup': 20 / 60.0, # unsure about this, might be lower
    'fsf.recovery': 0 / 60.0
}

class Bellina(Adv):
    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+Howling_to_the_Heavens()
    conf['slots.poison.a'] = Twinfold_Bonds()+The_Plaguebringer()
    conf['slots.d'] = Fatalis()
    conf['acl'] = """
        `s2, sim_duration-now()<1.5
        `s3, not self.s3_buff
        if self.dragondrive_buff.get()
        `s1, self.dragonform.dragon_gauge>1000 and x=3
        `fsf, x=3
        else
        `s2
        `dragon
        `fs, x=4
        end
    """
    coab = ['Ieyasu','Curran','Berserker']

    def fs_proc_alt(self, e):
        with CrisisModifier(e.name, 1.00, self.hp):
            self.dmg_make('fs', 5.65)
        self.dragonform.charge_gauge(self.conf.fs.utp, utp=True)

    def l_dragondrive_x(self, e):
        xalt = self.dragondrive_x
        xseq = e.name
        dmg_coef = xalt.conf[xseq].dmg
        sp = xalt.conf[xseq].sp
        hit = xalt.conf[xseq].hit
        utp = xalt.conf[xseq].utp
        log('x', xseq, 'dragondrive')
        self.hits += hit
        with CrisisModifier('x', 1.00, self.hp):
            self.dmg_make(xseq, dmg_coef)
        self.charge(xseq, sp)
        self.dragonform.charge_gauge(utp, utp=True)

    def prerun(self):
        self.dragondrive_buff = Selfbuff('dragondrive', 0.35, -1, 's', 'passive')
        self.dragonform.set_dragondrive(self.dragondrive_buff)
        Event('dragon_end').listener(self.dragondrive_on) # cursed
        Event('dragondrive_end').listener(self.dragondrive_off)

        self.dragondrive_x = X_alt(self, 'dragondrive', dragondrive_auto_conf, x_proc=self.l_dragondrive_x)
        self.fs_alt = Fs_alt(self, Conf(dragondrive_fs_conf), self.fs_proc_alt)

        self.a3_str = Modifier('a3', 'att', 'passive', 0.20)
        self.a3_spd = Spdbuff('a3',0.10,-1)
        
        self.a_s1 = self.s1.ac
        self.a_s1a = S('s1', Conf({'startup': 0.10, 'recovery': 1.10}))

        self.a_s2 = self.s2.ac
        self.a_s2a = S('s2', Conf({'startup': 0.10, 'recovery': 2.70}))

        self.fsf_a = Fs('fsf', self.conf.fsf)

    def dragondrive_on(self, e):
        self.s1.ac = self.a_s1a
        self.s2.ac = self.a_s2a
        self.fs_alt.on(-1)
        self.dragondrive_x.on()
        self.a_fsf = Fs('fsf', self.conf.fsf)

    def dragondrive_off(self, e):
        self.s1.ac = self.a_s1
        self.s2.ac = self.a_s2
        self.fs_alt.off()
        self.dragondrive_x.off()

    def s1_proc(self, e):
        if self.dragondrive_buff.get():
            with CrisisModifier(e.name, 0.50, self.hp):
                self.dmg_make(e.name, 2.02 * 5)
                self.hits += 5
            self.s1.charge(self.conf.s1.sp)
            self.dragonform.add_drive_gauge_time(self.s1.ac.getstartup()+self.s1.ac.getrecovery(), skill_pause=True)
            self.dragonform.charge_gauge(-750, utp=True)
        else:
            with CrisisModifier(e.name, 0.50, self.hp):
                self.dmg_make(e.name, 8.40)
                self.hits += 1

    def s2_proc(self, e):
        if self.dragondrive_buff.get():
            with CrisisModifier(e.name, 2.00, self.hp):
                self.dmg_make(e.name, 12.12)
                self.hits += 1
            self.dragonform.charge_gauge(-3000, utp=True)
            # -3000 gauge
            # 2.7666666507720947 (?)
            # 1212 mod, 3x crisis
        else:
            self.dragonform.charge_gauge(1200, utp=True)
            # 1 hp loss = 1 gauge gain, will assume 3000 max hp here
            if self.hp > 30:
                self.dragonform.charge_gauge(3000 * (self.hp-30)/100, utp=True)
                self.set_hp(30)
                self.a3_str.on()
                self.a3_spd.on()
            # regular buff duration (?)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)