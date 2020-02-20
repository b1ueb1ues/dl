import adv.adv_test
from core.advbase import *

def module():
    return Malora

class Malora(Adv):
    a1 = ('bk',0.2)
    conf = {}
    conf['acl'] = """
        `s1, cancel
        `s2, cancel
        `s3, cancel
        `fs, x=4
        """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
