import adv.adv_test
from core.advbase import *
from module.bleed import Bleed
from slot.a import *
from slot.d import *

def module():
    return Botan

class Botan(Adv):
#    comment = "RR+Jewels"
    a3 = ('prep_charge','5%')
    conf = {}
    conf['slots.a'] = RR() + BN()
    conf['slots.d'] = Shinobi()
    conf['acl'] = """
        `s2, pin='prep' or fsc
        `s1, (x=5 or fsc) and this.bleed._static['stacks']<3
        `s3, x=5 or fsc
        `fs, x=5
        """

    def init(this):
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc
    
    def prerun(this):
        this.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(this, e):
        Bleed("s1", 1.46).on()

    def c_s2_proc(this, e):
        Teambuff('s2',0.1,15,'crit','chance').on()

    def s2_proc(this, e):
        Selfbuff('s2',0.1,15,'crit','chance').on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)


