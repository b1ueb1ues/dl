from core.advbase import *
from module.x_alt import Fs_alt

def module():
    return Fritz

class Fritz(Adv):
    conf = {}
    conf['acl'] = """
        `dragon
        `s1, x=5 and cancel or fsc
        `s2
        `s3
        `fs, x=5
        """
    coab = ['Blade','Halloween_Elisanne','Peony']

    def fs_proc_alt(self, e):
        self.afflics.stun('fs', 100)

    def prerun(self):
        conf_fs_alt = {'fs.dmg': 4.03, 'fs.hit': 11}
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)

    def s2_proc(self, e):
        self.fs_alt.on(3)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)