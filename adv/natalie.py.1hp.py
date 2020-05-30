from core.advbase import *
import adv.natalie
from slot.a import HoH, Primal_Crisis

def module():
    return Natalie

class Natalie(adv.natalie.Natalie):
    conf = adv.natalie.Natalie.conf.copy()
    conf['slots.a'] = HoH()+Primal_Crisis()

    def prerun(self):
        super().prerun()
        self.set_hp(0)
        self.a3atk.on()
        self.a3spd.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Natalie, *sys.argv)