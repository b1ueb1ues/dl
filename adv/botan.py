import adv_test
from adv import *
from module.bleed import Bleed
from slot.a import *
from slot.d import *

def module():
    return Botan

class Botan(Adv):
#    comment = "RR+Jewels"
    a3 = ('prep','50%')
    conf = {}
    conf['slots.a'] = RR() + Jewels_of_the_Sun()
    conf['slots.d'] = Shinobi()

    def init(this):
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc
    
    def prerun(this):
        this.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(this, e):
        Bleed("s1_bleed", 1.44).on()

    def c_s2_proc(this, e):
        Teambuff('s2',0.1,15,'crit','chance').on()

    def s2_proc(this, e):
        Selfbuff('s2',0.1,15,'crit','chance').on()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, fsc
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2,mass=0)


