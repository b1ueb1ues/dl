from core.advbase import *
import melody
from slot.a import *
from slot.d import *

def module():
    return Melody

class Melody(Adv):
    comment = 'no s2; Freyja'
    a1 = ('cc',0.08,'hp100')

    conf = {}
    conf['slots.a'] = A_Dogs_Day()+Castle_Cheer_Corps()
    conf['slots.d'] = Freyja()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Melody, *sys.argv)