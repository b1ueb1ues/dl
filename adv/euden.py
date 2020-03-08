import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Euden

class Euden(Adv):
    a1 = ('dc', 4)
    conf = {}
    conf['slot.d'] = Dreadking_Rathalos()
    conf['slot.a'] = The_Shining_Overlord()+Elegant_Escort()

    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, x=2 and s1.charged > self.sp_val(3)+self.sp_val('fs')
        `fs, x=3
        """
    conf['afflict_res.burn'] = 0

    def s1_proc(self, e):
        self.afflics.burn('s1',110,0.883)
        self.dragonform.charge_gauge(3)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
    # logcat([str(type(Euden.conf['slot.d']).__name__)])