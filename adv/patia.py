import adv_test
from adv import *
from module.bleed import Bleed
from slot.a import *
from slot.d import *

def module():
    return Patia

class Patia(Adv):
    a1 = ('bt',0.35)
    a3 = ('primed_crit_chance',(0.10,5))

    def prerun(this):
        this.bleed = Bleed("g_bleed",0).reset()
        this.a3_iscding = 0

    def s1_proc(this, e):
        Event('defchain')()
        #Teambuff('s1',0.10,9.375).on()

    def s2_proc(this, e):
        Bleed("s2_bleed", 1.46).on()

if __name__ == '__main__':
    conf = {}
    conf['slots.a'] = VC()+Luck_of_the_Draw()
    conf['slot.d'] = Shinobi()
    conf['acl'] = """
        `s1
        `s2
        `s3, seq=5
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)


