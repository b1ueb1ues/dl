import adv_test
import adv
from slot.a import *

def module():
    return Linus

class Linus(adv.Adv):
    comment = 'do not use weapon skill'
    pass

if __name__ == '__main__':
    conf = {}
    conf['slot.a'] = KFM()+FitF()
    conf['acl'] = """
        `s1 
        `s2
        `s3,seq=4
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

