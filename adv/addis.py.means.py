from core.advbase import *
from adv import addis
from module.bleed import mBleed
from slot.a import *

def module():
    return Addis

class Addis(addis.Addis):
    def prerun(self):
        self.s2buff = Selfbuff('s2_shapshifts1',1, 10,'ss','ss')
        self.s2str = Selfbuff('s2_str',0.25,10)
        self.bleedpunisher = Modifier('bleed','att','killer',0.08)
        self.bleedpunisher.get = self.getbleedpunisher
        self.bleed = mBleed('g_bleed',0).reset()


    def s1_proc(self, e):
        if self.s2buff.get():
            self.s2buff.buff_end_timer.timing += 2.5
            self.s2str.buff_end_timer.timing += 2.5
            mBleed(e.name, 1.32).on()
        else:
            self.afflics.poison(e.name,100,0.53)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Addis, *sys.argv)