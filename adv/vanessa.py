import adv_test
import adv
from slot.a import *

def module():
    return Vanessa

class Vanessa(adv.Adv):
    comment = ''
    a1 = ('fs',0.4)
    a3 = ('lo',0.3)
    
    conf = {}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = KFM()+JotS()
        else:
            this.conf.slot.a = KFM()+CE()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `s3, seq=4
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

