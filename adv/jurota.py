from core.advbase import *
from slot.d import *

def module():
    return Jurota

class Jurota(Adv):
    a1 = ('bk',0.2)

    conf = {}
    conf['slot.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1
        `s2, seq=5
        `s3
    """
    coab = ['Wand', 'Xander', 'Dagger']
    

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)