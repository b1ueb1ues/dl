from core.advbase import *
import d_xainfried

def module():
    return Dragonyule_Xainfried

class Dragonyule_Xainfried(d_xainfried.Dragonyule_Xainfried):
    conf = {}
    def d_slots(self):
        self.slots.d = slot.d.Freyja()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(d_xainfried, *sys.argv)
