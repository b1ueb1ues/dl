from core.advbase import *
from slot.a import *
from slot.d import *
def module():
    return Vanessa

class Vanessa(Adv):
    comment = ''
    a1 = ('fs',0.4)
    a3 = ('lo',0.3)
    conf = {}
    conf['slots.d'] = Dreadking_Rathalos()
    conf['slots.a'] = Kung_Fu_Masters()+Mega_Friends()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1, cancel
        `s2, fsc
        `fs, x=4
    """
    coab = ['Blade', 'Serena', 'Marth']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)