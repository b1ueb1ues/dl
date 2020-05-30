from core.advbase import *
import adv.bellina

def module():
    return Bellina

class Bellina(adv.bellina.Bellina):

    def prerun(self):
        super().prerun()
        self.set_hp(0)
        self.a3_str.on()
        self.a3_spd.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Bellina, *sys.argv)