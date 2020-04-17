import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Raemond

class Raemond(Adv):
    conf = {}
    conf['slots.a'] = TSO()+BN()
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

