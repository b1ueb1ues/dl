from core.advbase import *
from slot.a import *

def module():
    return Valentines_Ezelith

class Valentines_Ezelith(Adv):
    a1 = ('ecombo',35)
    a3 = ('bk',0.2)

    conf = {}
    conf['slots.a'] = Forest_Bonds()+Elegant_Escort()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, seq=4
    """
    coab = ['Blade', 'Marth', 'Serena']
    conf['afflict_res.burn'] = 0

    def s1_proc(self, e):
        self.afflics.burn(e.name,110,0.883)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
