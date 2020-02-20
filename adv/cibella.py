import adv.adv_test
from core.advbase import *
import slot.a 
from slot.a import *
from slot.d import *

def module():
    return Cibella

class Cibella(Adv):
    conf = {}
    conf['acl'] = """
        `s2
        `s3, seq=5
        `fs, seq=5
        """
    #conf['slots.a'] = RR() + Saintly_Delivery()
    #comment = 'reach 100 resist with Saintly Delivery'
    conf['slots.d'] = DJ()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
