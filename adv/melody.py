from core.advbase import *
from slot.a import *
from slot.d import *
from module.x_alt import Fs_alt

def module():
    return Melody

class Melody(Adv):
    a1 = ('cc',0.15,'hp100')

    conf = {}
    conf['slots.a'] = A_Dogs_Day()+From_Whence_He_Comes()
    conf['slots.d'] = Ariel()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s4
        `fs, x=5
    """
    coab = ['Bow','Tobias','Dagger2']
    share = ['Dragonyule_Xainfried']

    def prerun(self):
        conf_fs_alt = {
            'fs.dmg':3.40,
            'fs.recovery': 72 / 60.0, # needs confirm
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt))

    def s1_proc(self, e):
        self.fs_alt.on(1)

    def s2_proc(self, e):
        self.afflics.poison(e.name, 120, 0.582)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)