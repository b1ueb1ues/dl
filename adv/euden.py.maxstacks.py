if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *
from slot.d import *
import euden

def module():
    return Euden

class Euden(euden.Euden):
    a1 = ('dc_max', (0.10, 0.15, 0.15))
    def d_slots(self):
        self.conf.slot.a = The_Shining_Overlord_Max_Stacks()+EE()
        self.conf.slot.d = Apollo()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

