from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Marty

class Marty(Adv):
    a1 = ('sp',0.05)

    conf = {}
    conf['slots.a'] = The_Wyrmclan_Duo()+Primal_Crisis()
    conf['slots.burn.a'] = Resounding_Rendition()+Elegant_Escort()
    conf['acl'] = """
        `dragon, s
        `s3, fsc and not self.s3_buff
        `s1, fsc
        `fs, x=2
        """
    coab = ['Blade', 'Serena', 'Marth']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)