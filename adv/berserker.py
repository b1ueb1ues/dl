import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Berserker

class Berserker(Adv):
    a3 = ('lo',0.3)
    conf = {}
    conf['acl'] = """
        `s1
        `s3, fsc
        `fs, seq=2 and cancel
        """

    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = TSO()+JotS()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

