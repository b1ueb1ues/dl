if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from adv import *
from core.log import *
from slot.a import *

def module():
    return Alfonse

class Alfonse(adv.Adv):
    a1 = ('lo',0.50*10.0/15.0)
    a3 = ('sp',0.08)
    conf = {}
    conf['slot.a'] = TSO()+BN()
    conf['acl'] = """
        `s1
        `s2,fsc
        `s3,fsc 
        `fs, seq=3
        """

    def s1_before(this, e):
        adv.Selfbuff('s1buff',0.15,10).on()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

