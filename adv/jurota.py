from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Jurota

class Jurota(Adv):
    a1 = ('bk',0.2)

    conf = {}
    conf['slots.frostbite.a'] = Primal_Crisis() + His_Clever_Brother()
    conf['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1
        `s2, seq=5
        `s3
    """
    coab = ['Tiki', 'Xander', 'Dagger']
    
if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)