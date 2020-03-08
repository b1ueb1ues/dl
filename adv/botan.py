import adv.adv_test
from core.advbase import *
from module.bleed import Bleed
from slot.a import *
from slot.d import *

def module():
    return Botan

class Botan(Adv):
#    comment = "RR+Jewels"
    a3 = ('prep_charge',0.05)
    conf = {}
    conf['slots.a'] = RR() + BN()
    conf['slots.d'] = Shinobi()
    conf['acl'] = """
        `s2, pin='prep' or fsc
        `s1, (x=5 or fsc) and self.bleed._static['stacks']<3
        `s3, x=5 or fsc
        `fs, x=5
        """

    def init(self):
        if self.condition('buff all team'):
            self.s2_proc = self.c_s2_proc
    
    def prerun(self):
        self.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(self, e):
        Bleed("s1", 1.46).on()

    def c_s2_proc(self, e):
        Teambuff('s2',0.1,15,'crit','chance').on()

    def s2_proc(self, e):
        Selfbuff('s2',0.1,15,'crit','chance').on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


