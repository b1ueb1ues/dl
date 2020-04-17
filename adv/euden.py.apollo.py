import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
import adv.euden
def module():
    return Euden

class Euden(adv.euden.Euden):
    comment = 'DKR > Apollo if more than 1 burn user'
    a1 = ('dc', 4)
    conf = adv.euden.Euden.conf.copy()
    conf['slots.d'] = Apollo()
    conf['acl'] = """
        `dragon
        `s3, fsc and not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, x=3
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)