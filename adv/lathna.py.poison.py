import adv_test
import lathna
from slot.a import *

def module():
    return Lathna

class Lathna(lathna.Lathna):
    comment = ''
    def prerun(this):
        super().prerun()
        from adv_test import sim_duration
        if this.condition('always poisoned'):
            this.afflics.poison.resist=0
            this.afflics.poison.on('always_poisoned', 1, 0, duration=sim_duration, iv=sim_duration)

    def d_slots(this):
        this.slots.a = RR()+The_Plaguebringer()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

