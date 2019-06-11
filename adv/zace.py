import adv_test
from adv import *
from slot.a import *

def module():
    return Zace

class Zace(Adv):
    #comment = 'RR+Jewels'
    a1 = ('s',0.2)
    conf = {}
    conf['slot.a'] = Jewels_of_the_Sun() + RR()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

