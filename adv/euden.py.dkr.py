import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
import adv.euden
def module():
    return Euden

class Euden(adv.euden.Euden):
    comment = 'c3fs c2fs c2fs s1; DKR > Apollo if more than 1 burn user'
    a1 = ('dc', 4)
    conf = adv.euden.Euden.conf.copy()
    conf['slots.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, x=2 and s1.charged > self.sp_val(3)+self.sp_val('fs')
        `fs, x=3
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)