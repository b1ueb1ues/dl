import adv_test
from adv import *

def module():
    return Irfan

class Irfan(Adv):
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3, seq=5
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

