from core.advbase import *
from slot.a import *

def module():
    return Vanessa

class Vanessa(Adv):
    a1 = ('fs',0.4)
    a3 = ('lo',0.3)
    
    conf = {}
    conf['slots.a'] = The_Wyrmclan_Duo()+Primal_Crisis()
    conf['slots.burn.a'] = Primal_Crisis()+Elegant_Escort()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1, cancel
        `s2, x=4
        `fs, x=5
    """
    coab = ['Blade', 'Marth', 'Serena']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
