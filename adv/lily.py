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
        `dragon, cancel
        `s4
        `s3
        `s2
        `s1, seq=5 and cancel
    """
    coab = ['Blade', 'Dagger', 'Tiki']
    share = ['Gala_Elisanne', 'Ranzal']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)