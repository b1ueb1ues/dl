import adv_test
import lathna
from slot.a import *

def module():
    return Lathna

class Lathna(lathna.Lathna):
    comment = ''
    def prerun(this):
        super().prerun()
        if this.condition('always poisoned'):
            this.poisoned=True
        else:
            this.poisoned=False

    def d_slots(this):
        this.conf.slot.a = RR()+The_Plaguebringer_Always_Poisoned()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

