import adv.adv_test
from core.advbase import *
from module.bleed import mBleed as Bleed
from slot.d import *
from slot.a import *
from adv import victor

def module():
    return Victor

class Victor(victor.Victor):
    def prerun(self):
        random.seed()
        self.bleed = Bleed("g_bleed",0).reset()


    def s1_proc(self, e):
        Bleed("s1", 1.46).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

