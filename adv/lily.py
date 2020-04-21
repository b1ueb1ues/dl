from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Lily

class Lily(Adv):
    a1 = ('a',0.15,'hp100')
    a3 = ('prep','100%')

    conf = {}
    conf['slots.a'] = CC()+Seaside_Princess()
    conf['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5 and cancel
        `s3, s
        `s2, pin='prep'
        """
    coab = ['Blade', 'Dagger', 'Xainfried']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)