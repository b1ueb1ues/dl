from core.advbase import *
from slot.a import *

def module():
    return Alain

class Alain(Adv):
    conf = {}
    conf['slots.a'] = Primal_Crisis()+Elegant_Escort()
    conf['acl'] = """
        `dragon.act('s end')
        `s3, not self.s3_buff
        `s1, cancel
        `s2, cancel
        `fs, x=5
        """
    conf['afflict_res.burn'] = 0
    coab = ['Blade', 'Wand', 'Marth']

    def s1_proc(self, e):
        self.afflics.burn('s1',100,0.803)
    
    def s2_proc(self, e):
        self.afflics.burn('s2',100,0.803)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)