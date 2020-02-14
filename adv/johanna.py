import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Johanna

class Johanna(Adv):
    conf = {}
    conf['slot.a'] = KFM()+CE()
    conf['acl'] = """
        `s1 
        `s2 
        `s3
        `fs,seq=5
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

