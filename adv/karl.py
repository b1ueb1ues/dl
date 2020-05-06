from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Karl

class Karl(Adv):
    a1 = ('a',0.08,'hit15')
    a3 = ('a',0.15,'hp70')

    conf = {}
    conf['slots.a'] = Primal_Crisis()+The_Lurker_in_the_Woods()
    conf['slots.d'] = Gala_Mars()
    conf['acl'] = """
        `dragon, s=2
        `s3, not self.s3_buff
        `s2, cancel
        `fs, x=2
    """
    coab = ['Blade', 'Tiki', 'Bow']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)