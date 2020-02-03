import adv.adv_test
from adv import *
from module.bleed import Bleed
from slot.a import *
from slot.d import *

def module():
    return Victor

class Victor(Adv):
    a1 = ('a',0.13,'hp70')
    conf = {}
    conf['slots.a'] = slot.a.RR()+slot.a.Jewels_of_the_Sun()
    conf['acl'] = """
        # bs = this.bleed._static['stacks']
        `s1
        `s2, seq=5
        `s3, seq=5
        """

    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = HoH()+JotS()

    def prerun(this):
        random.seed()
        this.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(this, e):
        if random.random() < 0.8:
            Bleed("s1_bleed", 1.46).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2, mass=1)

