from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Valentines_Ezelith

class Valentines_Ezelith(Adv):
    a1 = ('ecombo',35)
    a3 = ('bk',0.2)
    conf = {}
    conf['slots.a'] = Dear_Diary()+Elegant_Escort()
    conf['slots.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `dragon
        `s3, fsc and not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, seq=2
    """
    conf['afflict_res.burn'] = 0
    coab = ['Blade', 'Serena', 'Marth']

    def s1_proc(self, e):
        self.afflics.burn('s1',110,0.883)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)