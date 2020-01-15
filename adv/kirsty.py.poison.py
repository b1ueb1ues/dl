import adv_test
from adv import *
import kirsty
from slot.a import *

def module():
    return Kirsty

class Kirsty(kirsty.Kirsty):
    comment = ''
    def d_slots(this):
        this.slots.a = RR()+The_Plaguebringer()

    def prerun(this):
        super().prerun()
        from adv_test import sim_duration
        if this.condition('always poisoned'):
            this.afflics.poison.resist=0
            this.afflics.poison.on('always_poisoned', 1, 0, duration=sim_duration, iv=sim_duration)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)