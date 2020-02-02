if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *

def module():
    return Vanessa

class Vanessa(adv.Adv):
    comment = ''
    a1 = ('fs',0.4)
    a3 = ('lo',0.3)
    conf = {}
    conf['slot.a'] = KFM()+CE()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1 
        `s2 
        `fs,seq=5
        """
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = KFM()+JotS()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

