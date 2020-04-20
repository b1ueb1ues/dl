from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Yue

class Yue(Adv):
    conf = {}
    conf['slots.a'] = Breakfast_at_Valerios()+Resounding_Rendition()
    conf['slots.burn.a'] = Primal_Crisis()+Elegant_Escort()
    conf['slots.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `dragon, s=2
        `s3, not self.s3_buff
        `s1, cancel
        `s2, fsc
        `fs, x=4
        """
    coab = ['Blade', 'Marth', 'Halloween_Mym']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)