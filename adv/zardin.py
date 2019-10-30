if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *
from slot.d import *

def module():
    return Zardin

class Zardin(adv.Adv):
    a1 = ('a',0.10,'hp100')
    
    conf = {}
    conf['slot.a'] = TSO()+JotS()
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """

    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = TSO()+BN()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

