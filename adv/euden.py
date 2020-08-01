from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Euden

class Euden(Adv):
    a1 = ('dc', 4)
    
    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+Me_and_My_Bestie()
    conf['slots.d'] = Gala_Mars()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `s4, fsc
        `fs, x=3
    """
    coab = ['Blade', 'Dagger2', 'Yuya']
    conf['afflict_res.burn'] = 0
    share = ['Ranzal']

    def s1_proc(self, e):
        self.afflics.burn(e.name,110,0.883)
        self.dragonform.charge_gauge(30)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)