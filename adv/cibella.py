import adv_test
from adv import *
import slot.a 
from slot.a import *

def module():
    return Cibella

class Cibella(Adv):
    conf = {}
    conf['slots.a'] = RR() + Saintly_Delivery()
    comment = 'reach 100 resist with Saintly Delivery'


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)
