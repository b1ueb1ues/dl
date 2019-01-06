import adv_test
from adv import *

def module():
    return Cibella

class Cibella(Adv):
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

