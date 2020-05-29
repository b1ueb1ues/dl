from core.advbase import *
from slot.a import *

def module():
    return Xania

class Xania(Adv):
    a1 = ('s',0.35)

    conf = {}
    conf['slots.a'] = Candy_Couriers()+Elegant_Escort()
    conf['acl'] = """
        `dragon, s=2
        `s3, not self.s3_buff
        `s1
        `s2, x=5
    """
    coab = ['Blade', 'Marth', 'Joe']
    conf['afflict_res.burn'] = 0

    def s1_proc(self, e):
        self.afflics.burn(e.name,100,0.803)

    def s2_proc(self, e):
        self.afflics.burn(e.name,100,0.803)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
