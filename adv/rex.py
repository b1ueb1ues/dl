import adv_test
import adv
from slot.a import *

def module():
    return Rex

class Rex(adv.Adv):
    conf = {}
    conf['slots.a'] = KFM()+JotS()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `s3
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

