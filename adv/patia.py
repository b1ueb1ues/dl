import adv.adv_test
from core.advbase import *
from module.bleed import Bleed
from slot.a import *

def module():
    return Patia

class Patia(Adv):
    a1 = ('bt',0.35)
    a3 = ('primed_crit_chance', 0.10, 5)

    conf = {}
    conf['slots.a'] = VC()+Jewels_of_the_Sun()
    conf['acl'] = """
        `s1
        `s2
        `s3, x=5
        `fs, x=5
        """

    def prerun(this):
        this.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(this, e):
        Teambuff('s1', 0.25, 15, 'defense').on()
        #Teambuff('s1',0.10,9.375).on()

    def s2_proc(this, e):
        Bleed("s2", 1.46).on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
