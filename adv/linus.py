import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Linus

class Linus(Adv):
    # comment = 'do not use weapon skill'
    conf = {}
    conf['slots.a'] = KFM()+FitF()
    conf['acl'] = """
        `s1 
        `s2
        `s3,seq=4
        `fs,seq=5
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

