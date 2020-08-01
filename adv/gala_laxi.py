from core.advbase import *
from slot.a import *
from module.x_alt import X_alt

def module():
    return Gala_Laxi

# 2x crisis mods on autos and fs
galaxi_autos = {
    'x1.dmg': 0.77,
    'x1.sp': 172,
    'x1.cp': 1,
    'x1.startup': 0.20,
    'x1.recovery': 0.30,
    'x1.hit': 2,

    'x2.dmg': 0.846,
    'x2.sp': 172,
    'x2.cp': 1,
    'x2.startup': 0.1667,
    'x2.recovery': 0.3333,
    'x2.hit': 2,

    'x3.dmg': 0.924,
    'x3.sp': 315,
    'x3.cp': 1,
    'x3.startup': 0.1667,
    'x3.recovery': 0.3333,
    'x3.hit': 2,

    'x4.dmg': 1.46,
    'x4.sp': 344,
    'x4.cp': 2,
    'x4.startup': 0.1667,
    'x4.recovery': 0.3333,
    'x4.hit': 3,
}

galaxi_ex_autos = {
    'x1.dmg': 1.055,
    'x1.sp': 216,
    'x1.cp': 1,
    'x1.startup': 0.20,
    'x1.recovery': 0.30,
    'x1.hit': 5,

    'x2.dmg': 1.16,
    'x2.sp': 216,
    'x2.cp': 1,
    'x2.startup': 0.1667,
    'x2.recovery': 0.3333,
    'x2.hit': 5,

    'x3.dmg': 1.265,
    'x3.sp': 396,
    'x3.cp': 1,
    'x3.startup': 0.1667,
    'x3.recovery': 0.3333,
    'x3.hit': 5,

    'x4.dmg': 1.64,
    'x4.sp': 432,
    'x4.cp': 2,
    'x4.startup': 0.1667,
    'x4.recovery': 0.3333,
    'x4.hit': 6,
}

galaxi_fs = {
    'fs.dmg': 1.548,
    'fs.sp': 288,
    'fs.cp': 1,
    'fs.charge': 0.15,
    'fs.startup': 0.2667,
    'fs.recovery': 0.5,
    'fs.hit': 6,

    'fsf.charge': 0.15,
    'fsf.startup': 0.2667,
    'fsf.recovery': 0,
}

class Gala_Laxi(Adv):    
    conf = galaxi_fs.copy()
    conf['slots.a'] = Twinfold_Bonds()+Me_and_My_Bestie()
    conf['acl'] = """
        # `norm
        `ex
        `dragon
        `s3, not self.s3_buff
        `s2
        `s1
        `s4
        """
    conf['afflict_res.burn'] = 0
    coab = ['Blade', 'Marth', 'Serena']
    share = ['Ranzal']

    def init(self):
        self.slots.c.coabs['Dagger'] = [None, 'dagger2']

    def prerun(self):
        self.eden_mode = False
        self.eden_mode_timer = Timer(self.eden_mode_off, 20)
        self.fig = Timer(self.fig_dmg, 0.33, True).on()
        self.stance = 'norm'
        self.next_stance = 'norm'
        self.stance_dict = {
            'norm': X_alt(self, 'norm', galaxi_autos, x_proc=self.l_stance_x),
            'ex': X_alt(self, 'ex', galaxi_ex_autos, x_proc=self.l_stance_x)
        }
        self.update_stance()
        self.a1_cp = 0
        self.a1_buffs = {
            33: Selfbuff('a1_defense', 0.20, -1, 'defense', 'buff'),
            66: Selfbuff('a1_sd', 0.15, -1, 's', 'buff'),
            100: Selfbuff('a1_str', 0.15, -1, 'att', 'buff'),
        }
        self.a3_crit_chance = 0
        self.a3_crit_dmg = 0
        self.crit_mod = self.custom_crit_mod

    def norm(self):
        return self.queue_stance('norm')

    def ex(self):
        return self.queue_stance('ex')

    def custom_crit_mod(self, name):
        if self.a3_crit_dmg > 9 or name == 'test':
            return self.solid_crit_mod(name)
        else:
            crit = self.rand_crit_mod(name)
            if crit == 1:
                Selfbuff('a3_crit_dmg',0.04,-1,'crit','damage').on()
                self.a3_crit_dmg += 1
            return crit

    def eden_mode_off(self, t):
        self.fig.off()
        self.eden_mode = False
        self.update_a1(-100)

    def fig_dmg(self, t):
        if any([abs(ac.status) == 1 for ac in (self.s1.ac, self.s2.ac)]):
            self.dmg_make('fig', 1.00, 'x')

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.eden_mode = False

    def queue_stance(self, stance):
        if self.stance != stance and self.next_stance != stance and not self.skill._static.silence:
            log('stance', stance, 'queued')
            self.next_stance = stance
            self.update_stance()
            return True
        return False

    def update_stance(self):
        if self.next_stance is not None:
            curr_stance = self.stance_dict[self.stance]
            next_stance = self.stance_dict[self.next_stance]
            next_stance.switch(curr_stance)
            self.stance = self.next_stance
            self.next_stance = None

    def update_a1(self, delta):
        if not self.eden_mode:
            next_cp = max(min(self.a1_cp+delta, 100), 0)
            delta = next_cp - self.a1_cp
            if delta == 0:
                return
            if delta > 0:
                for thresh, buff in self.a1_buffs.items():
                    if self.a1_cp < thresh and next_cp >= thresh:
                        buff.on()
            else:
                for thresh, buff in self.a1_buffs.items():
                    if next_cp < thresh:
                        buff.off()
            self.a1_cp = next_cp
        log('debug', 'cp', self.a1_cp)

    def l_stance_x(self, e):
        xalt = self.stance_dict[self.stance]
        xseq = e.name
        dmg_coef = xalt.conf[xseq].dmg
        sp = xalt.conf[xseq].sp
        cp = xalt.conf[xseq].cp
        hit = xalt.conf[xseq].hit
        log('x', xseq, self.stance)
        self.hits += hit
        self.dmg_make(xseq, dmg_coef)
        self.charge(xseq, sp)
        self.update_a1(cp * hit)
        self.update_stance()

    def dmg_proc(self, name, amount):
        if self.a3_crit_chance < 3 and self.condition('always connect hits') and self.hits // 15 > self.a3_crit_chance:
            self.a3_crit_chance = self.hits // 15
            Selfbuff('a3_crit_chance',0.04,-1,'crit','chance').on()

    def s1_proc(self, e):
        if self.eden_mode:
            self.hits += 12
            self.dmg_make(e.name, 10.91)
            self.afflics.burn(e.name,120,0.97)
        else:
            self.hits += 4
            self.dmg_make(e.name, 8.432)
    
    def s2_proc(self, e):
        if self.eden_mode:
            self.dmg_make(e.name, 22.96)
        else:
            self.eden_mode_timer.on()
            self.fig.on()
            self.eden_mode = True

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
