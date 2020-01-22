import adv_test
import ieyasu
from slot.a import *

def module():
    return Ieyasu

class Ieyasu(ieyasu.Ieyasu):
    comment = ''
    def prerun(this):
        super().prerun()
        if this.condition('always poisoned'):
            this.poisoned=True
        else:
            this.poisoned=False

    def d_slots(this):
        this.conf.slot.a = HoH()+The_Plaguebringer_Always_Poisoned()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)
    adv_test.sum_ac()
