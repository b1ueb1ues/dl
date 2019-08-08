import adv.adv_test
from adv import *

def module():
    return Ryozen

class Ryozen(Adv):
    a3 = ('od',0.08)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

