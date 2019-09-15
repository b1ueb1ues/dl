import adv_test
import adv
from slot.a import *


def module():
    return Karl

class Karl(adv.Adv):
    a3 = ('a',0.08,'hp70')
    conf = {}
    conf['slot.a'] = TSO()+BN()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3,fsc
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0)

