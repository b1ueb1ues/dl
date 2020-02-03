import adv.adv_test
from adv import *
import d_xainfried

def module():
    return D_Xainfried

class D_Xainfried(d_xainfried.D_Xainfried):
    conf = {}
    def d_slots(this):
        this.slots.d = slot.d.Freyja()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)
