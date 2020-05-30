from core.advbase import *
from slot.d import *
from slot.a import *


def module():
    return Emma

class Emma(Adv):
    a1 = ('bt',0.25)
    a3 = ('primed_att', 0.05)

    conf = {}
    conf['slots.d'] = Gala_Mars()
    conf['slots.a'] = Castle_Cheer_Corps()+From_Whence_He_Comes()
    conf['slots.burn.a'] = conf['slots.a']
    conf['acl'] = """
        `dragon.act('c1 s s end'), s=1
        `fs, self.fs_prep_c==3
        `s4, cancel
        `s1
        `s3
        `fs, x=5
        """
    coab = ['Tobias', 'Tiki', 'Bow']
    share = ['Patia','Summer_Luca']

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.buff_class = Dummy if adv.slots.c.ele != 'flame' else Teambuff if adv.condition('buff all team') else Selfbuff

    def s1_proc(self, e):
        self.buff_class(e.name,0.25,15).on()

    def s2_proc(self, e):
        Event('defchain')()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)