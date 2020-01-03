if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import Amulet, Elegant_Escort
from slot.d import *
import euden

class The_Shining_Overlord(Amulet):
    att = 65
    a = [('dc_max', (0.06, 0.09, 0.15)), ('s',0.40)]

def module():
    return Euden

class Euden(euden.Euden):
    comment = '70% dragon\'s claw buff'
    a1 = ('dc_max', (0.10, 0.15, 0.15))
    def d_slots(self):
        self.conf.slot.a = The_Shining_Overlord()+Elegant_Escort()
        self.conf.slot.d = Apollo()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

