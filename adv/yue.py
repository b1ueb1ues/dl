import adv_test
import adv
from slot.a import *
from slot.d import *

def module():
    return Yue

class Yue(adv.Adv):
    #comment = 'Arctos'
    conf = {}
    #conf['slot.d'] = Arctos()




if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2,seq=4
        `s3,seq=4
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

