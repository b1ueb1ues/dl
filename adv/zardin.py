from core.advbase import *
from slot.a import *

def module():
    return Zardin

class Zardin(Adv):
    a1 = ('a',0.20,'hp100')
    
    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+Primal_Crisis()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s3, cancel
        `s4, fsc
        `s1, fsc
        `s2, fsc
        `fs, seq=3 and cancel
        """
    coab = ['Blade', 'Dagger', 'Yurius']
    share = ['Gala_Elisanne', 'Ranzal']

    def s1_proc(self, e):
        self.afflics.frostbite(e.name,120,0.41)

    def s2_proc(self, e):
        self.afflics.frostbite(e.name,120,0.41)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)