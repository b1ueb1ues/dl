import adv_test
import adv
from slot.d import *

def module():
    return Rex

class Rex(adv.Adv):

    def d_slots(this):
        #this.conf.slot.d = DJ()
        return

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `s3
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

