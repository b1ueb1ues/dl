from core.advbase import *
from slot.a import *
from slot.d import *
from module.x_alt import Fs_alt

def module():
    return Peony

peony_conf = {
    'x3.recovery': 44/60.0, # c4 0.9523809552192688 -> 0.761904776096344, need confirm
}

class Peony(Adv):
    comment = 'team skill prep not considered'
    a3 = ('k_paralysis',0.30)

    conf = peony_conf.copy()
    conf['slots.a'] = Valiant_Crown()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon, fsc
        `fs, s2.charged>=s2.sp and self.fs_alt.uses > 0
        `s1, x=5
        `s2, cancel
        `s3, cancel
    """
    coab = ['Blade','Sharena','Malora']
    conf['afflict_res.paralysis'] = 0

    def d_coabs(self):
        if self.duration <= 60:
            self.coab = ['Tiki','Sharena','Malora']

    def fs_proc_alt(self, e):
        self.fs_str.on()
        self.fs_spd.on()
        Event('defchain')()
        self.a1_is_cd = True
        self.a1_cd_timer.on(20)

    def a1_cd(self, t):
        self.a1_is_cd = False
        if self.a1_charge_defer:
            self.fs_alt.on(1)
            self.a1_charge_defer = False

    def prerun(self):
        self.s1_shift = 0
        conf_fs_alt = {
            'fs.dmg':0,
            'fs.sp' :0,
            'fs.charge': 30/60.0,
            'fs.startup': 20/60.0,
            'fs.recovery': 60/60.0,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        self.fs_str = Teambuff('fs_str',0.10,10,'att','buff')
        self.fs_spd = Spdbuff('fs_spd',0.10,10,wide='team')

        self.a1_is_cd = False
        self.a1_charge_defer = False
        self.a1_cd_timer = Timer(self.a1_cd)

    @staticmethod
    def prerun_skillshare(self, dst_key):
        self.a1_is_cd = False
        self.fs_alt = Dummy()

    def s1_proc(self,e):
        self.afflics.paralysis(e.name,120,0.97)
        if self.s1_shift > 0:
            Event('defchain')()
        if self.s1_shift > 1:
            Teambuff(e.name,0.10,10,'att','buff').on()
        self.s1_shift = (self.s1_shift + 1) % 3

    def s2_proc(self,e):
        with KillerModifier('s2_killer','hit',0.2,['paralysis']):
            self.dmg_make(e.name,9.64)
        Spdbuff(f'{e.name}_spd',0.10,10,wide='team').on()
        Teambuff(f'{e.name}_str',0.10,10,'att','buff').on()

        if self.a1_is_cd:
            self.a1_charge_defer = True
        else:
            self.fs_alt.on(1)

        # Using Gentle Dream grants the user the \"Empowering Dreams\" effect. 
        # When this effect is active, the user's next force strike will fill 40% of skill gauges for each team member's initial skill (with the exception of Peony), and grant the following effects to all team members for 10 seconds, none of which will stack: 
        # Increases strength by 10% 
        # Increases attack rate by 10% 
        # Increases defense by 20% 
        # Adds 5% to shadow resistance 
        # Increases movement speed by 5%. 
        # The Empowering Dreams effect cannot stack, will be consumed on use, and will not activate again for 20 seconds after activating.

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None,*sys.argv)