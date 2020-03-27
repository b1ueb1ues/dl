from core.advbase import *
from slot.a import *
from slot.d import *

galex_conf = {
    'x1.dmg': 82 / 100.0,
    'x1.startup': 8 / 60.0,
    'x1.recovery': 34 / 60.0,
    'x1.hit': 1,

    'x2.dmg': 88 / 100.0,
    'x2.startup': 0,
    'x2.recovery': 28 / 60.0,
    'x2.hit': 1,

    'x3.dmg': 104 / 100.0,
    'x3.startup': 0,
    'x3.recovery': 19 / 60.0,
    'x3.hit': 1,

    'x4.dmg': 110 / 100.0,
    'x4.startup': 0,
    'x4.recovery': 33 / 60.0,
    'x4.hit': 1,

    'x5.dmg': 165 / 100.0,
    'x5.startup': 0,
    'x5.recovery': 49 / 60.0,
    'x5.hit': 1,
}

def module():
    return Gala_Alex

class Skill_Reservoir(Skill):

    def __init__(self, name=None, conf1=None, conf2=None):
        super().__init__(name, conf1)
        self.conf_tpl = (conf1, conf2)
        self.ac_tpl = (
            S('s1', conf1),
            S('s2', conf2)
        )
        self.chain_timer = Timer(self.chain_off)
        self.chain_status = 0

    def chain_on(self, skill, timeout=3):
        self.chain_status = skill
        self.chain_timer.on(timeout)

    def chain_off(self, t=None):
        self.chain_status = 0

    def charge(self, sp):
        self.charged = min(self.sp*3, self.charged + sp)
        if self.charged >= self.sp*3:
            self.skill_charged()

    @property
    def count(self):
        return self.charged // self.sp

    def __call__(self, call=0):
        self.conf = self.conf_tpl[call]
        self.ac = self.ac_tpl[call]
        if self.cast() and self.count == 0 and self.chain_timer.online:
            self.chain_timer.off()
            self.chain_status = 0

class Gala_Alex(Adv):
    comment = 'no bk bonus in sim'
    a3 = ('k_poison', 0.30)

    conf = galex_conf.copy()
    conf['slot.d'] = Shinobi()
    conf['slot.a'] = The_Shining_Overlord()+The_Fires_of_Hate()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s2, not self.afflics.poison.get()
        `s1, not self.s1_debuff.get() or self.sr.count > 1
        `fs, x=2
    """
    conf['afflict_res.poison'] = 0

    def prerun(self):
        self.s1_debuff = Debuff('s1', 0.05, 15)

        self.a1_k = Modifier('a1', 'killer', 'passive', 0.30)
        self.a1_k.get = self.a1_get
        self.a1_k.on()

        self.sr = Skill_Reservoir('s1', self.conf.s1, self.conf.s2)
        # cursed
        self.s1.cast = lambda: self.sr(0)
        self.s2.cast = lambda: self.sr(1)

    def charge_p(self, name, percent):
        percent = percent / 100 if percent > 1 else percent
        self.sr.charge(self.sp_convert(percent, self.conf.sr.sp))
        self.s3.charge(self.sp_convert(percent, self.conf.s3.sp))
        log('sp', name, f'{percent*100:.0f}%', f'{self.sr.charged}/{self.sr.sp}, {self.s3.charged}/{self.s3.sp}')
        self.think_pin('prep')

    def charge(self, name, sp):
        # sp should be integer
        sp = self.sp_convert(self.sp_mod(name), sp)
        self.sr.charge(sp)
        self.s3.charge(sp)
        self.think_pin('sp')
        log('sp', name, sp, f'{self.sr.charged}/{self.sr.sp} ({self.sr.count}), {self.s3.charged}/{self.s3.sp}')

    def a1_get(self):
        return (self.mod('def') != 1) * 0.30

    def s1_proc(self, e):
        if self.sr.chain_status == 0:
            self.dmg_make('s1', 2.02)
            self.s1_debuff.on()
            self.dmg_make('s1', 2.02*2)
            self.hits += 3
        elif self.sr.chain_status > 0:
            k = 1 + (self.mod('def') != 1) * 0.1
            self.dmg_make('s1', 2.02*3*k)
            self.dmg_make('s1', 4.85*k)
            self.hits += 4
        # elif self.sr.chain_status == 2:
        #     k = 1 + (self.mod('def') != 1) * 0.1
        #     self.dmg_make('s1', 2.02*3)
        #     self.dmg_make('s1', 4.85*k)
        #     self.hits += 4
        #     break only
        #     352.5 * 3 + 987
        self.sr.chain_on(1)

    def s2_proc(self, e):
        if self.sr.chain_status == 0:
            self.dmg_make('s2', 5.53)
            self.afflics.poison('s2', 120, 0.582)
            self.hits += 1
        elif self.sr.chain_status > 0:
            with Modifier('s2_killer', 'poison_killer', 'hit', 0.1):
                self.dmg_make('s2', 5.53)
                self.dmg_make('s2', 4.42)
                self.hits += 2
        # elif self.sr.chain_status == 2:
        #     self.dmg_make('s2', 5.53)
        #     with Modifier('s2_killer', 'poison_killer', 'hit', 0.1):
        #         self.dmg_make('s2', 4.42)
        #     break only
        #     972 * 2
        self.sr.chain_on(2)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)