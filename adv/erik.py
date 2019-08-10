if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *

def module():
    return Erik

class Erik(adv.Adv):
    comment =''
    a1 = ('fs',0.30)
    conf = {}
    conf['acl'] = """
    `s1
    `s2,fsc
    `s3,fsc
    `fs,seq=5
    """

    #comment += '& reach 100 resist with Silke Lends a Hand'
    #conf = {'slots.a': RR()+Silke_Lends_a_Hand()}



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

