import adv_test
import adv
from adv import *
from core.log import *
from slot.a import *

def module():
    return Audric

class Audric(adv.Adv):
    conf = {}
    conf['slot.a'] = TSO()+BN()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, fsc
        `s3, fsc
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0)

