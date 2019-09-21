if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from module.bleed import mBleed as Bleed
from slot.d import *
from slot.a import *
from adv import victor

def module():
    return Victor

class Victor(victor.Victor):
    def prerun(this):
        random.seed()
        this.bleed = Bleed("g_bleed",0).reset()


    def s1_proc(this, e):
        Bleed("s1_bleed", 1.46).on()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2, mass=0)

