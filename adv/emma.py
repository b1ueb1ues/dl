import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *


def module():
    return Emma

class Emma(Adv):
    a1 = ('bt',0.25)
    a3 = ('primed_att', 0.05)

    conf = {}
    conf['slots.d'] = Dreadking_Rathalos()
    conf['slots.a'] = Castle_Cheer_Corps()+FWHC()
    conf['acl'] = """
        `fs, self.fs_prep_c==3
        `s3, not self.s3_buff
        `s1, cancel
        `fs, x=5
        """

    def init(self):
        if self.condition('buff all team'):
            self.s1_proc = self.c_s1_proc


    def c_s1_proc(self, e):
        Teambuff('s2',0.25,15).on()

    def s1_proc(self, e):
        Selfbuff('s2',0.25,15).on()

    def s2_proc(self, e):
        Event('defchain')()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

