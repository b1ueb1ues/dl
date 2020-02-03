import adv.adv_test
from adv import *

def module():
    return Aeleen

class Aeleen(Adv):
    conf = {}

    conf['acl'] = """
        `s1
        `s3, fsc
        `fs, seq=5
        """
    a1 = ('bt',0.25)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

