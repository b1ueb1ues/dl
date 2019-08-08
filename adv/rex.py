if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

import adv
from slot.d import *
from slot.a import *

def module():
    return Rex

class Rex(adv.Adv):
    conf = {}
    conf['slot.a'] = KFM()+CE()
    conf['acl'] = """
        `s1 
        `s2 
        `s3
        `fs,seq=5
        """

    def d_slots(this):
        #this.conf.slot.d = DJ()
        return

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

