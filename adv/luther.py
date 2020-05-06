from core.advbase import *
from slot.d import *

def module():
    return Luther

class Luther(Adv):
    a1 = ('cc',0.10,'hit15')

    conf = {}
    conf ['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
    """
    coab = ['Blade', 'Xander', 'Tiki']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)