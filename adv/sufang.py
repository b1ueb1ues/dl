import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *
from module.x_alt import Fs_alt

def module():
    return Su_Fang

class Su_Fang(Adv):
    a3 = ('s',0.35)
    conf = {}
    conf['slot.d'] = Garland()
    conf['slot.a'] = Twinfold_Bonds()+The_Fires_of_Hate()
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3
        `fs, seq=5
        """

    def fs_proc_alt(self, e):
        self.afflics.poison('s2_fs', REPLACE, 0.582)

    def prerun(self):
        conf_fs_alt = {}
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)

    def s1_proc(self, e):
        with KillerModifier('skiller', 'hit', REPLACE, ['poison']):
            self.dmg_make('s1', REPLACE)

    def s2_proc(self, e):
        self.fs_alt.on(1)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

