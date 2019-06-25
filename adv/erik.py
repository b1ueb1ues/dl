import adv_test
import adv
from slot.a import *

def module():
    return Erik

class Erik(adv.Adv):
    comment = 'c1+fs'

    conf = {}
    conf['slot.a'] = KFM() + FP()

    a1 = ('fs',0.30)

    #comment += '& reach 100 resist with Silke Lends a Hand'
    #conf = {'slots.a': RR()+Silke_Lends_a_Hand()}


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s3, fsc
        `s2, fsc
        `fs, seq=1
        """
    adv_test.test(module(), conf, verbose=0)
