import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Rex

class Rex(Adv):
    conf = {}
    conf['slots.a'] = KFM()+CE()
    conf['acl'] = """
        `s1 
        `s2,seq=4
        `s3,seq=4
        `fs,seq=5
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

