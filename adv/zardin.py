import adv_test
import adv
from slot.a import *
from slot.d import *

def module():
    return Zardin

class Zardin(adv.Adv):
    a1 = ('a',0.10,'hp100')
    
    conf = {}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = TSO()+BN()
        else:
            this.conf.slot.a = TSO()+JotS()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

