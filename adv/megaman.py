import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
from module.bleed import Bleed, mBleed

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
    'fs.startup': 45 / 60.0, # 30 charge 15 hit
    'fs.recovery': 60 / 60.0,
    'fs.hit': 1,

    'x1fs.startup': 60 / 60.0, # fs cannot cancel x recovery
    'x2fs.startup': 60 / 60.0,
    'x3fs.startup': 60 / 60.0,
    'x4fs.startup': 60 / 60.0,
    'x5fs.startup': 60 / 60.0,

    # s1 related
    's1.ammo': 2000,
    's1.x.startup': 0.2, # 1 saw = 12f 
    's1.x.recovery': 0,
    's1.x.dmg': 0.5,
    's1.x.hit': 1,
    's1.x.cost': 200,
    # s1 bleed: 132% mod 50% chance

    # s2 related
    's2.ammo': 4000,
    's2.x.startup': 0.5 * 6, # hits every 30f starting from 0f, auto release after 5 rounds
    's2.x.recovery': 0,
    's2.x.dmg': 1.00,
    's2.x.hit': 16, # HDT sized enemy
    's2.x.cost': 1000,
}

class Skill_Ammo(Skill):
    def __init__(self, name=None, conf=None, ac=None):
        super().__init__(name, conf, ac)
        self.current_ammo = self.conf.ammo
        self.ammo = self.conf.ammo
        self.cost = self.conf.x.cost
        self.is_active = False
    
    def check(self):
        return self.current_ammo >= self.cost

    def charge_ammo(self, ammo):
        self.current_ammo = min(self.ammo, self.current_ammo + ammo)

class Mega_Man(Adv):
    comment = '16 hits leaf shield (max 32 hits)'

    a1 = ('od', 0.15) # this is the coab
    conf = megaman_conf.copy()
    conf['slot.d'] = Cerberus()
    conf['slot.a'] = Primal_Crisis()+Dear_Diary()
    conf['acl'] = """
        # check_s(n) means neither s1 or s2 are active, and s[n] has full ammo
        `s3, not this.s3_buff
        `s1, this.check_s(1) and this.bleed._static['stacks']<3
        `s2, this.s1.is_active and this.bleed._static['stacks']>=3
        `s1, this.s1.is_active and this.bleed._static['stacks']>=3
    """
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
        return self.dmg_make('d_ds',self.dragonform.conf.ds.dmg,'s')

    def init(self):
        # self.conf += Conf(megaman_conf)
        del self.slots.c.ex['wand']

    def prerun(self):
        self.s1 = Skill_Ammo('s1', self.conf.s1)
        self.a_s1x = X('s1x', self.conf.s1.x)
        self.l_s1_x = Listener('x',self.l_megaman_s1_x).off()
        self.s2 = Skill_Ammo('s2', self.conf.s2)
        self.a_s2x = X('s1x', self.conf.s2.x)
        self.l_s2_x = Listener('x',self.l_megaman_s2_x).off()

        self.fs_normal = self.fs
        
        random.seed()
        self.bleed = Bleed('g_bleed', 0).reset()
        self.bleed.quickshot_event.dname = 'x_s1_bleed'
        self.bleed.true_dmg_event.dtype = 'x'
        self.bleed_chance = 0.5

    def proc_bleed(self):
        if random.random() <= self.bleed_chance:
            self.bleed = Bleed('x', 1.32)
            self.bleed.quickshot_event.dname = 'x_s1_bleed'
            self.bleed.true_dmg_event.dtype = 'x'
            self.bleed.on()

    def charge_p(this, name, sp):
        percent = sp
        this.s3.charge(this.ceiling(this.conf.s3.sp*percent))
        log('sp', name, '{:.0f}%   '.format(percent*100),'%d/%d, %d/%d, %d/%d'%(\
            this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp) )
        this.think_pin('prep')

    def charge(self, name, sp):
        sp = int(sp) * self.float_problem(self.sp_mod(name))
        sp = self.float_problem(sp)
        sp = self.ceiling(sp)
        self.s3.charge(sp)
        self.think_pin('sp')

        # ammo
        self.s1.charge_ammo(self.conf[name.split('_')[0]].ammo)
        self.s2.charge_ammo(self.conf[name.split('_')[0]].ammo)

        log('sp', name, sp,'%d/%d, %d/%d, %d/%d'%(\
            self.s1.current_ammo, self.s1.ammo, self.s2.current_ammo, self.s2.ammo, self.s3.charged, self.s3.sp))

    def alt_x_on(self, s, alt_l_x, alt_a_x):
        self.l_x.off()
        alt_l_x.on()
        self.fs = self.fs_off
        self.x1 = alt_a_x
        self.x2 = alt_a_x
        self.x3 = alt_a_x
        self.x4 = alt_a_x
        self.x5 = alt_a_x
        s.is_active = True

    def alt_x_off(self, s, alt_l_x):
        alt_l_x.off()
        self.l_x.on()
        self.fs = self.fs_normal
        self.x1 = self.a_x1
        self.x2 = self.a_x2
        self.x3 = self.a_x3
        self.x4 = self.a_x4
        self.x5 = self.a_x5
        s.is_active = False

    def s1_proc(self, e):
        if self.s2.is_active:
            self.alt_x_off(self.s2, self.l_s2_x)

        if self.s1.is_active:
            log('debug', 's1_turn_off')
            self.alt_x_off(self.s1, self.l_s1_x)
        else:
            self.alt_x_on(self.s1, self.l_s1_x, self.a_s1x)

    def s2_proc(self, e):
        if self.s1.is_active:
            self.alt_x_off(self.s1, self.l_s1_x)

        if self.s2.is_active:
            log('debug', 's2x_turn_off')
            self.alt_x_off(self.s2, self.l_s2_x)
        else:
            self.alt_x_on(self.s2, self.l_s2_x, self.a_s2x)

    def l_range_x(this, e):
        if e.name == 's1x' or e.name == 's2x':
            return
        super().l_range_x(e)

    def l_megaman_s1_x(self, e):
        self.hits += self.conf.s1.x.hit
        self.dmg_make('o_x_metal_blade', self.conf.s1.x.dmg*self.conf.s1.x.hit)
        self.proc_bleed()
        self.s1.current_ammo -= self.s1.cost
        log('sp', 's1x', -self.s1.cost,'%d/%d, %d/%d, %d/%d'%(\
            self.s1.current_ammo, self.s1.ammo, self.s2.current_ammo, self.s2.ammo, self.s3.charged, self.s3.sp))
        if self.s1.current_ammo < self.s1.cost:
            log('debug', 's1x_depleted')
            self.alt_x_off(self.s1, self.l_s1_x)
        self.think_pin('x')

    def l_megaman_s2_x(self, e):
        self.hits += self.conf.s2.x.hit
        self.dmg_make('o_x_leaf_shield', self.conf.s2.x.dmg*self.conf.s2.x.hit)
        self.s2.current_ammo -= self.s2.cost
        log('sp', 's2x', -self.s2.cost,'%d/%d, %d/%d, %d/%d'%(\
            self.s1.current_ammo, self.s1.ammo, self.s2.current_ammo, self.s2.ammo, self.s3.charged, self.s3.sp))
        if self.s2.current_ammo < self.s2.cost:
            log('debug', 's2x_depleted')
            self.alt_x_off(self.s2, self.l_s2_x)
        self.think_pin('x')

    def fs_off(self):
        return False

    def check_s(self, s):
        if s == 's1' or s == 1:
            return self.s1.current_ammo >= self.s1.ammo and not self.s1.is_active and not self.s2.is_active
        elif s == 's2' or s == 2:
            return self.s2.current_ammo >= self.s2.ammo and not self.s1.is_active and not self.s2.is_active

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)