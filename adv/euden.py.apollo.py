import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *
import adv.euden
def module():
    return Euden

class Euden(adv.euden.Euden):
    comment = 'end first shift early; DKR > Apollo if more than 1 burn user'
    a1 = ('dc', 4)
    conf = adv.euden.Euden.conf.copy()
    conf['slot.d'] = Apollo()
    conf['acl'] = """
        `dragon.act("c3 s end"), this.dc_level<2
        `dragon, this.dc_level>=2
        `s3, fsc and not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `fs, x=3
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)