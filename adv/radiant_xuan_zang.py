from core.advbase import *
from slot.d import *
from slot.a import *
from module.x_alt import Fs_alt

def module():
    return Radiant_Xuan_Zang

staff_fs_conf = {
    'fs.dmg': 0.61*4,
    'fs.sp': 580,
    'fs.charge': 24 / 60.0,
    'fs.startup': 100 / 60.0,
    'fs.recovery': 40 / 60.0,
    'fs.hit': 4,

    'x1fs.charge': 33 / 60.0, # 9 delay + FS
    'x2fs.charge': 30 / 60.0, # 6 delay + FS
}

class Radiant_Xuan_Zang(Adv):
    a1 = ('prep', 100)
    a3 = ('dbt', 0.20)

    conf = staff_fs_conf.copy()
    conf['slots.a'] = Candy_Couriers()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon, x=1
        `s2
        `s1
        `s3, x=5
        `fs, self.fs_alt.uses>0 and cancel
    """
    coab = ['Sharena', 'Blade', 'Peony']
    conf['afflict_res.paralysis'] = 0

    def fs_proc_alt(self, e):
        self.afflics.paralysis.res_modifier = 0.20
        Timer(self.paralysis_rate_reset).on(20)

    def paralysis_rate_reset(self, t):
        self.afflics.paralysis.res_modifier = 0

    def prerun(self):
        conf_fs_alt = {'fs.dmg':8.88}
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        self.xihe_gauge = 0
        self.xihe = {'s1': False, 's2': False}
        if self.condition('buff all team'):
            self.xihe_gauge_gain = 50
            self.buff_class = Teambuff
        else:
            self.xihe_gauge_gain = 20
            self.buff_class = Selfbuff

    def s1_proc(self, e):
        if self.xihe[e.name]:
            self.xihe[e.name] = False
            with KillerModifier('s1_killer', 'hit', 0.5, ['paralysis']):
                self.dmg_make(e.name, 18.80)
            Debuff(e.name, 0.25, 10, 1, 'attack').on()
        else:
            self.dmg_make(e.name, 16.1)
            Debuff(e.name, 0.10, 10, 0.70, 'attack').on()
            self.afflics.paralysis(e.name,120,0.97)

    def s2_proc(self, e):
        if self.xihe[e.name]:
            self.xihe[e.name] = False
            self.buff_class(e.name, 0.20, 15).on()
            self.inspiration.add(5, team=True)
        else:
            self.xihe_gauge += self.xihe_gauge_gain
            log('debug', 'xihe', self.xihe_gauge)
            if self.xihe_gauge >= 100:
                self.xihe_gauge = 0
                self.fs_alt.on(1)
                self.xihe = {'s1': True, 's2': True}

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)