import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Lily

class Lily(Adv):
    a1 = ('a',0.15,'hp100')
    a3 = ('prep','100%')

    conf = {}
    conf['slot.a'] = CC()+Seaside_Princess()
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5 and cancel
        `s3, s
        `s2, pin='prep'
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)



