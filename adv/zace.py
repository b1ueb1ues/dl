import adv_test
from adv import *

def module():
    return Zace

class Zace(Adv):
    a1 = ('s',0.2)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

