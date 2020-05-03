from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Melody

class Melody(Adv):
    a1 = ('cc',0.08,'hp100')

    conf = {}
    conf['slots.a'] = A_Dogs_Day()+From_Whence_He_Comes()
    conf['slots.d'] = Ariel()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `fs, x = 5
    """
    coab = ['Bow','Tobias','Tiki']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)