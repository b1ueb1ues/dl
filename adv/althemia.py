import adv.adv_test
from core.advbase import *

def module():
    return Althemia

class Althemia(Adv):
    a1 = ('s',0.3,'hp100')
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

