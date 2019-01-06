import adv_test
from adv import *

def module():
    return Berserker

class Berserker(Adv):
    pass

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

