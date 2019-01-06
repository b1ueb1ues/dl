import adv_test
from adv import *

def module():
    return Malka

class Malka(Adv):
    comment = 'do not use fs'


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

