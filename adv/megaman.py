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
    'x1_missile.ammo': 50,
    'x1_missile.startup': 17/60.0,
    'x1_missile.recovery': 11/60.0,
    'x1.hit': 1,

    'x2.dmg': 0.30,
    'x2.sp': 80,
    'x2_missile.ammo': 50,
    'x2_missile.startup': 0,
    'x2_missile.recovery': 11/60.0,
    'x2.hit': 1,

    'x3.dmg': 0.30,
    'x3.sp': 80,
    'x3_missile.ammo': 50,
    'x3_missile.startup': 0,
    'x3_missile.recovery': 11/60.0,
    'x3.hit': 1,

    'x4.dmg': 0.30,
    'x4.sp': 80,
    'x4_missile.ammo': 50,
    'x4_missile.startup': 0,
    'x4_missile.recovery': 11/60.0,
    'x4.hit': 1,

    'x5.dmg': 0.30,
    'x5.sp': 80,
    'x5_missile.ammo': 50,
    'x5_missile.startup': 0,
    'x5_missile.recovery': 15/60.0,
    'x5.hit': 1,

    'fs.dmg': 0.9,
    'fs.sp': 400,
    'fs_missile.ammo': 180,
    'fs_missile.startup': 45 / 60.0, # 30 charge 15 hit
    'fs_missile.recovery': 60 / 60.0,
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
        return self.current_ammo > self.cost

    def charge_ammo(self, ammo):
        self.current_ammo = min(self.ammo, self.current_ammo + ammo)

class Mega_Man(Adv):
    comment = 'rollfs; means bleed; 16 hits leaf shield (HMS sized enemy)'

    a1 = ('od', 0.15) # this is the coab
    conf = {}
    conf['slot.d'] = Dreadking_Rathalos()
    conf['slot.a'] = Primal_Crisis()+Dear_Diary()
    conf['acl'] = """
        # check_s(n) means neither s1 or s2 are active, and s[n] has full ammo
        `s3, not this.s3_buff_on
        `s1, this.check_s(1)
        `s2, this.check_s(2)
        `dodge, fsc
        `fs
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

    conf['misc.means_bleed'] = True

    def init(self):
        self.conf += Conf(megaman_conf)
        del self.slots.c.ex['wand']

    def prerun(self):
        self.s1 = Skill_Ammo('s1', self.conf.s1)
        self.a_s1x = X('s1x', self.conf.s1.x)
        self.l_s1_x = Listener('x',self.l_megaman_s1_x).off()
        self.s2 = Skill_Ammo('s2', self.conf.s2)
        self.a_s2x = X('s2x', self.conf.s2.x)
        self.l_s2_x = Listener('x',self.l_megaman_s2_x).off()

        self.fs_normal = self.fs
        
        if self.conf.misc.means_bleed:
            self.bleed = mBleed('x', 1.32, 0.5).reset()
            self.bleed_chance = 1
        else:
            random.seed()
            self.bleed = Bleed('x', 1.32).reset()
            self.bleed_chance = 0.5
        self.bleed.quickshot_event.dname = 'x_s1_bleed'
        self.bleed.true_dmg_event.dtype = 'x'

    def proc_bleed(self):
        if self.bleed_chance == 1:
            self.bleed.on()
        elif random.random() <= self.bleed_chance:
            self.bleed.on()

    def charge_p(self, name, sp):
        if type(sp) == str and sp[-1] == '%':
            percent = int(sp[:-1])
            self.s3.charge(self.ceiling(self.conf.s3.sp*percent/100))
            log('sp', name, '%d%%   '%percent,'%d/%d, %d/%d, %d/%d'%(\
                self.s1.charged, self.s1.sp, self.s2.charged, self.s2.sp, self.s3.charged, self.s3.sp) )
            self.think_pin('prep')
            return

    def charge(self, name, sp):
        sp = int(sp) * self.float_problem(self.sp_mod(name))
        sp = self.float_problem(sp)
        sp = self.ceiling(sp)
        self.s3.charge(sp)
        self.think_pin('sp')

        # ammo
        self.s1.charge_ammo(self.conf[name].ammo)
        self.s2.charge_ammo(self.conf[name].ammo)

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
        if self.s1.is_active:
            log('debug', 's1_turn_off')
            self.alt_x_off(self.s1, self.l_s1_x)
        else:
            self.alt_x_on(self.s1, self.l_s1_x, self.a_s1x)
        if self.s2.is_active:
            self.s2.is_active = False

    def s2_proc(self, e):
        if self.s2.is_active:
            log('debug', 's2x_turn_off')
            self.alt_x_off(self.s2, self.l_s2_x)
        else:
            self.alt_x_on(self.s2, self.l_s2_x, self.a_s2x)
        if self.s1.is_active:
            self.s1.is_active = False

    def l_megaman_s1_x(self, e):
        self.hits += self.conf.s1.x.hit
        self.dmg_make('o_x_s1', self.conf.s1.x.dmg*self.conf.s1.x.hit)
        self.proc_bleed()
        self.s1.current_ammo -= self.s1.cost
        log('sp', 's1x', -self.s1.cost,'%d/%d, %d/%d, %d/%d'%(\
            self.s1.current_ammo, self.s1.ammo, self.s2.current_ammo, self.s2.ammo, self.s3.charged, self.s3.sp))
        if self.s1.current_ammo == 0:
            log('debug', 's1x_depleted')
            self.alt_x_off(self.s1, self.l_s1_x)
        self.think_pin('x')

    def l_megaman_s2_x(self, e):
        self.hits += self.conf.s2.x.hit
        self.dmg_make('o_x_s2', self.conf.s2.x.dmg*self.conf.s2.x.hit)
        self.s2.current_ammo -= self.s2.cost
        log('sp', 's2x', -self.s2.cost,'%d/%d, %d/%d, %d/%d'%(\
            self.s1.current_ammo, self.s1.ammo, self.s2.current_ammo, self.s2.ammo, self.s3.charged, self.s3.sp))
        if self.s2.current_ammo == 0:
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