import adv.adv_test
from core.advbase import *
from slot.a import *
import random
from slot.d import *

def module():
    return Xuan_Zang

class Xuan_Zang(Adv):
    a3 = ('cc',0.06,'hp70')
    conf = {}
    conf['slot.d'] = Dreadking_Rathalos()
    conf['slot.a'] = RR()+Jewels_of_the_Sun()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1, fsc
        `s2, cancel
        `fs, seq=4
        """

    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = RR()+JotS()

    def s1_proc(self, e):
        if self.mod('def')!= 1:
            self.dmg_make('o_s1_boost',2.51*3*0.2*0.91)

    def s2_proc(self, e):
        Debuff('s2_defdown',0.1,20,0.7).on()





if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

