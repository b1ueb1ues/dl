import adv_test
from adv import *
from slot.a import *

def module():
    return Alain

class Alain(Adv):
    comment = 'reach 100 resist with Saintly Delivery'
    def pre(this):
        this.slots.a = RR()+Saintly_Delivery()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

