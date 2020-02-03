import adv.adv_test
import adv
from slot.a import *

def module():
    return Raemond

class Raemond(adv.Adv):
    conf = {}
    conf['slot.a'] = TSO()+BN()
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

