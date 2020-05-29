from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Lea

class Lea(Adv):
    a1 = ('fs', 0.50)
    a3 = ('sp', 0.12, 'fs')
        
    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+Elegant_Escort()
    conf['acl'] = """
        `dragon, fsc
        `s3, not self.s3_buff
        `s1, fsc
        `fs, x=2
        """
    conf['afflict_res.burn'] = 0
    coab = ['Blade', 'Wand', 'Marth']
    
    def s1_proc(self, e):
        self.afflics.burn(e.name,120,0.97)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)