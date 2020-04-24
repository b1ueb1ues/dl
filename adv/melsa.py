from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Melsa

class Melsa(Adv):
    a3 = ('cc',0.08,'hit15')

    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+Stellar_Show()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, x=2
    """
    coab = ['Blade', 'Serena', 'Marth']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)