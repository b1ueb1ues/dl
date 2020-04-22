from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Yuya

class Yuya(Adv):
    a3 = ('primed_crit_chance', 0.5,5)
    
    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+The_Lurker_in_the_Woods()
    conf['slots.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `dragon
        `s3, fsc and not self.s3_buff
        `s1, fsc
        `fs, x=2
        """
    coab = ['Blade', 'Serena', 'Marth']

    def prerun(self):
        if self.condition('hp60'):
            Selfbuff('a1',0.2,-1,'att','passive').on()
        else:
            Selfbuff('a1',-0.2,-1,'att','passive').on()

    def s1_proc(self, e):
        Spdbuff("s2",0.2, 10)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)