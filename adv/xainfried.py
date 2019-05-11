import adv_test
from adv import *

def module():
    return Xainfried

class Xainfried(Adv):
    comment = 'use s1 only to cancel c5 of fs'
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)

