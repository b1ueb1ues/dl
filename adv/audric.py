if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from adv import *
from core.log import *
from slot.a import *

def module():
    return Audric

class Audric(adv.Adv):
    conf = {}
    conf['slot.a'] = TSO()+BN()
    conf['acl'] = """
        `s1
        `s2, fsc
        `fs, seq=3
        """

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

