from core.simulate import test_with_argv
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
    conf['slot.a'] = Twinfold_Bonds()+The_Plaguebringer()
    conf['acl'] = """
        `s2, fsc
        `s1
        `s3, fsc
        `fs, x=4
        """

    def fs_proc_alt(self, e):
        self.afflics.poison('fs', 120, 0.582)

    def prerun(self):
        conf_fs_alt = {'fs.dmg': 0.174, 'fs.hit': 6}
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        self.s2_buff = Selfbuff('s2', 0.30, 15)

    def s1_proc(self, e):
        with KillerModifier('skiller', 'hit', 0.50, ['poison']):
            self.dmg_make('s1', 5.58)
            if self.s2_buff.get():
                self.dmg_make('s1', 1.30)

    def s2_proc(self, e):
        self.fs_alt.on(1)
        self.s2_buff = Selfbuff('s2', 0.30, 15).on()


if __name__ == '__main__':
    test_with_argv('t_hope', *sys.argv)