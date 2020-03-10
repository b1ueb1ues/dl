import adv.adv_test
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
        `s1
        `s2
        `s3
        `fs, not self.afflics.poison.get() and self.fs_alt.uses > 0
    """
    conf['slot.d'] = Vayu()
    conf['slot.a'] = Dear_Diary() + The_Fires_of_Hate()
    conf['afflict_res.stun'] = 80
    conf['afflict_res.poison'] = 0

    def fs_proc_alt(self, e):
        self.afflics.stun('s2_fs', REPLACE+50)
        self.afflics.poison('s2_fs', REPLACE+50, 0.582)

    def prerun(self):
        conf_fs_alt = {REPLACE}
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        self.s2_mode = 0

    def s1_proc(self, e):
        with KillerModifier('s1killer', 'hit', REPLACE, ['stun']), KillerModifier('s1killer', 'hit', REPLACE, ['poison']):
            self.dmg_make('s1',REPLACE)

    def s2_proc(self, e):
        if self.s2_mode == 0:
            self.fs_alt.on(2)
        else:
            with KillerModifier('skiller', 'hit', REPLACE, ['poison']):
                self.dmg_make('s2',REPLACE)
        self.s2_mode = (self.s2_mode + 1) % 2


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)