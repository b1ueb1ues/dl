from core.advbase import *
from slot.a import Forest_Bonds, Primal_Crisis
import adv.valentines_addis

def module():
    return Valentines_Addis

class Valentines_Addis(adv.valentines_addis.Valentines_Addis):
    comment = 'no s2'

    conf = adv.valentines_addis.Valentines_Addis.conf.copy()
    def prerun(self):
        super().prerun()
        self.set_hp(0)
        self.a3atk.on()
        self.a3spd.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Valentines_Addis, *sys.argv)