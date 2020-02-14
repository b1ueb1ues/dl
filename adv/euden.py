import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Euden

class Euden(adv.Adv):
    a1 = ('dc', 4)
    conf = {}
    conf['slot.d'] = Dreadking_Rathalos()
    conf['slot.a'] = The_Shining_Overlord()+Elegant_Escort()

    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `fs, x=2 and s1.charged > this.sp_val(3)+this.sp_val('fs')
        `fs, x=3
        """
    conf['afflict_res.burn'] = 0

    def s1_proc(this, e):
        this.afflics.burn('s1',110,0.883)
        this.dragonform.charge_gauge(3)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
    # logcat([str(type(Euden.conf['slot.d']).__name__)])