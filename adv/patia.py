if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from module.bleed import Bleed
from slot.a import *

def module():
    return Patia

class Patia(Adv):
    a1 = ('bt',0.35)
    a3 = ('primed_crit_chance',(0.10,5))

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
        Event('defchain')()
        #Teambuff('s1',0.10,9.375).on()

    def s2_proc(this, e):
        Bleed("s2_bleed", 1.46).on()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)
