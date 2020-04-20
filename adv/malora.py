from core.advbase import *
from slot.a import *

def module():
    return Malora

class Malora(Adv):
    a1 = ('bk',0.2)
    
    conf = {}
    conf['slots.a'] = RR()+Breakfast_at_Valerios()
    conf['acl'] = """
        `dragon
        `s1
        `s2, cancel
        `s3, cancel
        `fs, x=4
        """
    coab = ['Blade','Wand','Halloween_Elisanne']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)