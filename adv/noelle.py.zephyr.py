import adv_test
import noelle
from slot.d import Zephyr

def module():
    return Noelle

class Noelle(noelle.Noelle):

    def d_slots(this):
        this.conf.slots.d = Zephyr()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

