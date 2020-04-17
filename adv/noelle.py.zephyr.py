import noelle
from slot.d import Zephyr

def module():
    return Noelle

class Noelle(noelle.Noelle):

    def d_slots(self):
        self.conf.slots.d = Zephyr()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Noelle, *sys.argv)