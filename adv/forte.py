from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Forte

class Forte(Adv):
    a3 = ('k_poison', 0.30)

    def s1_proc(self, e):
        with KillerModifier('s1_killer', 'hit', 0.3, ['poison']):
            self.dmg_make('s1', 11.34)

    def s2_proc(self, e):
        # 6.320000171661377 * 4
        with KillerModifier('s1_killer', 'hit', 0.3, ['poison']):
            self.dmg_make('s1', 11.34)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)