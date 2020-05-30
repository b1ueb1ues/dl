import adv.adv_test
from core.advbase import *
from adv import sazanka
from module.bleed import mBleed
from slot.d import *
from slot.a import *

def module():
    return Sazanka

class Sazanka(sazanka.Sazanka):
    def prerun(self):
        self.bleed = mBleed('g_bleed',0).reset()
        self.s2fscharge = 0

    def s1_proc(self, e):
        mBleed(e.name, 1.32).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
