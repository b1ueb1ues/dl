import adv_test
import adv
from slot.a import *

def module():
    return Marty

class Marty(adv.Adv):
    a1 = ('sp',0.05)
    #comment = 'reach 100 resist with Saintly Delivery'
    #import slot
    conf = {}
    conf['slots.a'] = TSO()+BN()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1,fsc
        `s3,fsc
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0)

