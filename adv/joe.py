from core.advbase import *
from slot.a import *

def module():
    return Joe

class Joe(Adv):
    a1 = ('edge_burn', 70, 'hp100')

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Elegant_Escort()
    conf['acl'] = """
        `dragon, s=1
        `s3, fsc and not self.s3_buff
        `s1
        `s2
        `fs, x=4
    """
    coab = ['Blade', 'Wand', 'Marth']
    conf['afflict_res.burn'] = 0

    def s1_proc(self, e):
        self.afflics.burn(e.name,100,0.803)
        
    def s2_proc(self, e):
        self.afflics.burn(e.name,100,0.803)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)