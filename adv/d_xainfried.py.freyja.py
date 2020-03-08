import adv.adv_test
from core.advbase import *
import d_xainfried

def module():
    return Dragonyule_Xainfried

class Dragonyule_Xainfried(d_xainfried.Dragonyule_Xainfried):
    conf = {}
    def d_slots(self):
        self.slots.d = slot.d.Freyja()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
