import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Zace

class Zace(Adv):
    a1 = ('s',0.2)
    conf = {}
    conf['slot.a'] = RR()+Jewels_of_the_Sun()
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

