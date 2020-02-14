import adv.adv_test
from core.advbase import *

def module():
    return Irfan

class Irfan(Adv):
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3, seq=5
        `fs, seq=5
        """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0, mass=0)

