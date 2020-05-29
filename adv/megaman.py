from core.advbase import *
from slot.a import *
from slot.d import *
from module.bleed import Bleed, mBleed
from module.x_alt import X_alt

def module():
    return Mega_Man

megaman_conf = {
    'x1.dmg': 0.30,
    'x1.sp': 80,
    'x1.ammo': 50,
    'x1.startup': 17/60.0,
    'x1.recovery': 11/60.0,
    'x1.hit': 1,

    'x2.dmg': 0.30,
    'x2.sp': 80,
    'x2.ammo': 50,
    'x2.startup': 0,
    'x2.recovery': 11/60.0,
    'x2.hit': 1,

    'x3.dmg': 0.30,
    'x3.sp': 80,
    'x3.ammo': 50,
    'x3.startup': 0,
    'x3.recovery': 11/60.0,
    'x3.hit': 1,

    'x4.dmg': 0.30,
    'x4.sp': 80,
    'x4.ammo': 50,
    'x4.startup': 0,
    'x4.recovery': 11/60.0,
    'x4.hit': 1,

    'x5.dmg': 0.30,
    'x5.sp': 80,
    'x5.ammo': 50,
    'x5.startup': 0,
    'x5.recovery': 15/60.0,
    'x5.hit': 1,

    'fs.dmg': 0.9,
    'fs.sp': 400,
    'fs.ammo': 180,
    'fs.charge': 30 / 60.0,
    'fs.startup': 15 / 60.0, # 30 charge 15 hit
    'fs.recovery': 60 / 60.0,
    'fs.hit': 1,

    'x1fs.charge': 45 / 60.0, # fs cannot cancel x recovery
    'x2fs.charge': 45 / 60.0,
    'x3fs.charge': 45 / 60.0,
    'x4fs.charge': 45 / 60.0,
    'x5fs.charge': 45 / 60.0,

    # s1 related
    's1.ammo': 2000,
    's1.x1.startup': 0.2, # 1 saw = 12f 
    's1.x1.recovery': 0,
    's1.x1.dmg': 0.5,
    's1.x1.hit': 1,
    's1.x1.cost': 200,
    # s1 bleed: 132% mod 50% chance

    # s2 related
    's2.ammo': 4000,
    's2.x1.startup': 0.5 * 6, # hits every 30f starting from 0f, auto release after 5 rounds
    's2.x1.recovery': 0,
    's2.x1.dmg': 1.00,
    's2.x1.hit': 16, # HDT sized enemy
    's2.x1.cost': 1000,
}

class Skill_Ammo(Skill):
    def __init__(self, name=None, conf=None, ac=None):
        super().__init__(name, conf, ac)
        self.current_ammo = self.conf.ammo
        self.ammo = self.conf.ammo
        self.cost = self.conf.x1.cost
    
    def check(self):
        return self.current_ammo >= self.cost

    def charge_ammo(self, ammo):
        self.current_ammo = min(self.ammo, self.current_ammo + ammo)

class Mega_Man(Adv):
    comment = '16 hits leaf shield (max 32 hits)'

    conf = megaman_conf.copy()
    conf['slots.d'] = Gala_Mars()
    conf['slots.a'] = Primal_Crisis()+Dear_Diary()
    conf['acl'] = """
        # check_s(n) means neither s1 or s2 are active, and s[n] has full ammo
        `dragon
        `s3, not self.s3_buff
        `s1, self.check_s(1) and self.bleed._static['stacks']<3
        `s2, self.s1_x.active and self.bleed._static['stacks']>=3
        `s1, self.s1_x.active and self.bleed._static['stacks']>=3
    """
    coab = ['Blade', 'Marth', 'Tiki']

    conf['dragonform'] = {
        'act': 'c5 s',

        'dx1.dmg': 1.20,
        'dx1.startup': 10 / 60.0, # c1 frames
        'dx1.hit': 3,

        'dx2.dmg': 1.20,
        'dx2.startup': 13 / 60.0, # c2 frames
        'dx2.hit': 3,

        'dx3.dmg': 1.20,
        'dx3.startup': 14 / 60.0, # c3 frames
        'dx3.hit': 3,

        'dx4.dmg': 1.20,
        'dx4.startup': 14 / 60.0, # c4 frames
        'dx4.hit': 3,

        'dx5.dmg': 1.20,
        'dx5.startup': 14 / 60.0, # c5 frames
        'dx5.recovery': 23 / 60.0, # recovery
        'dx5.hit': 3,

        'ds.dmg': 6.00,
        'ds.recovery': 113 / 60, # skill frames
        'ds.hit': 5,

        'dodge.startup': 45 / 60.0, # dodge frames
    }
    def ds_proc(self):
        return self.dmg_make('ds',self.dragonform.conf.ds.dmg,'s')

    def prerun(self):
        self.s1 = Skill_Ammo('s1', self.conf.s1)
        self.s1_x = X_alt(self, 's1', self.conf.s1, x_proc=self.l_megaman_s1_x, no_fs=True)
        # self.a_s1x = X('s1x', self.conf.s1.x)
        # self.l_s1_x = Listener('x',self.l_megaman_s1_x).off()
        self.s2 = Skill_Ammo('s2', self.conf.s2)
        self.s2_x = X_alt(self, 's2', self.conf.s2, x_proc=self.l_megaman_s2_x, no_fs=True)
        # self.a_s2x = X('s1x', self.conf.s2.x)
        # self.l_s2_x = Listener('x',self.l_megaman_s2_x).off()

        # self.fs_normal = self.fs
        
        random.seed()
        self.bleed = Bleed('g_bleed', 0).reset()
        self.bleed_chance = 0.5

    def proc_bleed(self):
        if random.random() <= self.bleed_chance:
            self.bleed = Bleed('o_metal_blade', 1.32)
            self.bleed.quickshot_event.dname = 'o_metal_blade_bleed'
            self.bleed.true_dmg_event.dtype = 'x'
            self.bleed.on()

    def charge(self, name, sp):
        sp = self.sp_convert(self.sp_mod(name), sp)
        # ammo
        self.s1.charge_ammo(self.conf[name.split('_')[0]].ammo)
        self.s2.charge_ammo(self.conf[name.split('_')[0]].ammo)
        self.s3.charge(sp)
        try:
            self.s4.charge(sp)
            log('sp', name, sp, f'{self.s1.current_ammo}/{self.s1.ammo}, {self.s2.current_ammo}/{self.s2.ammo}, {self.s3.charged}/{self.s3.sp}, {self.s4.charged}/{self.s4.sp}')
        except:
            log('sp', name, sp, f'{self.s1.current_ammo}/{self.s1.ammo}, {self.s2.current_ammo}/{self.s2.ammo}, {self.s3.charged}/{self.s3.sp}')
        self.think_pin('sp')

    def s1_proc(self, e):
        if self.s2_x.active:
            self.s2_x.off()

        if self.s1_x.active:
            self.s1_x.off()
        else:
            self.s1_x.on()

    def s2_proc(self, e):
        if self.s1_x.active:
            self.s1_x.off()

        if self.s2_x.active:
            self.s2_x.off()
        else:
            self.s2_x.on()

    # def l_range_x(self, e):
    #     if e.name == 's1x' or e.name == 's2x':
    #         return
    #     super().l_range_x(e)

    def l_megaman_s1_x(self, e):
        self.hits += self.conf.s1.x1.hit
        self.dmg_make('o_metal_blade', self.conf.s1.x1.dmg*self.conf.s1.x1.hit, 'x')
        self.proc_bleed()
        self.s1.current_ammo -= self.s1.cost
        log('sp', 'metal_blade', -self.s1.cost,'%d/%d, %d/%d, %d/%d'%(\
            self.s1.current_ammo, self.s1.ammo, self.s2.current_ammo, self.s2.ammo, self.s3.charged, self.s3.sp))
        if self.s1.current_ammo < self.s1.cost:
            self.s1_x.off()

    def l_megaman_s2_x(self, e):
        self.hits += self.conf.s2.x1.hit
        self.dmg_make('o_leaf_shield', self.conf.s2.x1.dmg*self.conf.s2.x1.hit, 'x')
        self.s2.current_ammo -= self.s2.cost
        log('sp', 'leaf_shield', -self.s2.cost,'%d/%d, %d/%d, %d/%d'%(\
            self.s1.current_ammo, self.s1.ammo, self.s2.current_ammo, self.s2.ammo, self.s3.charged, self.s3.sp))
        if self.s2.current_ammo < self.s2.cost:
            self.s2_x.off()

    def check_s(self, s):
        if s == 's1' or s == 1:
            return self.s1.current_ammo >= self.s1.ammo and not self.s1_x.active and not self.s2_x.active
        elif s == 's2' or s == 2:
            return self.s2.current_ammo >= self.s2.ammo and not self.s1_x.active and not self.s2_x.active

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)