from core.advbase import *
from slot.a import *
from slot.d.flame import *
def module():
    return Melsa

class Melsa(Adv):
    a3 = ('cc',0.08,'hit15')
    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+The_Lurker_in_the_Woods()
    conf['slots.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, x=2
    """
    coab = ['Blade', 'Wand', 'Marth']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)