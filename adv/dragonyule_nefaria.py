from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Dragonyule_Nefaria

class Dragonyule_Nefaria(Adv):
    a1 = ('s',0.25)
    
    conf = {}
    conf['slots.a'] = Primal_Crisis()+Mega_Friends()
    conf['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s3, fsc
        `s1, fsc
        `s4, fsc
        `fs, seq=4
    """
    coab = ['Blade', 'Xander', 'Thaniel']
    share = ['Gala_Elisanne', 'Ranzal']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)