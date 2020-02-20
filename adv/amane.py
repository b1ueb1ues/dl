import adv.adv_test
from core.advbase import *

def module():
    return Amane

class Amane(Adv):
    a3 = ('bk',0.2)
    a1 = ('prep','75%')
    conf = {}
    acl12 = """
        `s1
        `s2, seq=5 and cancel
        `s3
        """
    acl21 = """
        `s2
        `s1
        `s3, seq=5
        """ 
    conf['acl'] = acl21


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


