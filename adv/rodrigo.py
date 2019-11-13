import adv_test
import adv
from slot.a import *

def module():
    return Rodrigo

class Rodrigo(adv.Adv):
    a1 = ('a',0.08,'hp70')
    
    conf = {}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = TSO()+JotS()
        else:
            this.conf.slot.a = TSO()+BN()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

