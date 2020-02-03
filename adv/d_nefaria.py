import adv.adv_test
import adv
from slot.d import *

def module():
    return D_Nefaria

class D_Nefaria(adv.Adv):
    a1 = ('s',0.25)
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s3, fsc
        `fs, seq=4
        """
    conf['slots.d'] = DJ()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

