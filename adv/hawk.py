from core.simulate import test_with_argv
from core.advbase import *
from slot.a import *
from slot.d import *
from module.x_alt import Fs_alt

def module():
    return Hawk

class Hawk(Adv):
    a3 = [('k_stun',0.4), ('k_poison',0.3)]
    conf = {}
    conf['acl'] = """
        `fs, s=2
        `s2, s1.check()
        `s1, cancel
    """
    conf['slot.d'] = Vayu()
    conf['slot.a'] = Resounding_Rendition() + The_Fires_of_Hate()
    conf['afflict_res.stun'] = 80
    conf['afflict_res.poison'] = 0

    def fs_proc_alt(self, e):
        self.afflics.stun('fs', 110+50)
        self.afflics.poison('fs', 120+50, 0.582)

    def prerun(self):
        conf_fs_alt = {
            'fs.dmg': 4.94,
            'fs.hit':19,
            'fs.sp':2400,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        self.s2_mode = 0
        self.a_s2 = self.s2.ac
        self.a_s2a = S('s2', Conf({'startup': 0.10, 'recovery': 2.5}))

    def s1_proc(self, e):
        with KillerModifier('s1_stun_killer', 'hit', 3.3, ['stun']):
            self.dmg_make('s1',4.74)
        with KillerModifier('s1_poison_killer', 'hit', 2, ['poison']):
            self.dmg_make('s1',4.74)

    def s2_proc(self, e):
        if self.s2_mode == 0:
            self.fs_alt.on(2)
            self.s2.ac = self.a_s2a
        else:
            with KillerModifier('s2_killer', 'hit', 0.5, ['poison']):
                self.dmg_make('s2', 9.48)
            self.conf.s2.startup = 0.25
            self.conf.s2.recovery = 0.9
            self.s2.ac = self.a_s2
        self.s2_mode = (self.s2_mode + 1) % 2


if __name__ == '__main__':
    test_with_argv('t_hope', *sys.argv)