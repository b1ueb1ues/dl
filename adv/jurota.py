import adv.adv_test
import adv
from slot.a import *

def module():
    return Jurota

class Jurota(adv.Adv):
    a1 = ('bk',0.2)
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3
        """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

