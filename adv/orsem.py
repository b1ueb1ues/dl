import adv_test
from adv import *

def module():
    return Orsem

class Orsem(Adv):
    a1 = ('cc',0.10,'hit15')
    a3 = ('cc',0.06,'hp70')


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    adv_test.test(module(), conf, verbose=0, mass=0)

