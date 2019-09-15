import adv_test
import adv
from slot.a import *


def module():
    return Euden

class Euden(adv.Adv):
    conf ={}
    conf['slot.a'] = TSO()+BN()
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

