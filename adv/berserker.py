import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Berserker

class Berserker(Adv):
    a3 = ('lo',0.3)

    conf = {}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = TSO()+JotS()
            this.conf.slot.d = Shinobi()
        else:
            this.conf.slot.a = RR()+SS()
            this.conf.slot.d = Marishiten()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `fs, seq=2 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

