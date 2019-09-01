import adv_test
from adv import *
from module.bleed import mBleed as Bleed
from slot.d import *
from slot.a import *


def module():
    return Victor

class Victor(Adv):
    a1 = ('a',0.13,'hp70')
    conf = {}
    #conf['slots.a'] = slot.a.RR()+slot.a.Jewels_of_the_Sun()

   # def d_slots(this):
   #     if 'bow' in this.ex:
   #         this.conf.slot.a = RR()+JotS()


    def prerun(this):
        random.seed()
        this.bleed = Bleed("g_bleed",0).reset()


    def s1_proc(this, e):
        Bleed("s1_bleed", 1.46).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2,seq=5
        `s3,seq=5
        """
    adv_test.test(module(), conf, verbose=-2, mass=0)

