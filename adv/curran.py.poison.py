import adv_test
import curran
from slot.a import *
from slot.d import *

def module():
    return Curran

class Curran(curran.Curran):
    comment = ''
    def prerun(this):
        super().prerun()
        from adv_test import sim_duration
        if this.condition('always poisoned'):
            this.afflics.poison.resist=0
            this.afflics.poison.on('always_poisoned', 1, 0, duration=sim_duration, iv=sim_duration)

    def d_slots(this):
        this.slots.a = KFM()+The_Plaguebringer()
        this.slots.d = Shinobi()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)
