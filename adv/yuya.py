from core.advbase import *
from slot.a import *

def module():
    return Yuya

class Yuya(Adv):
    a3 = ('primed_crit_chance', 0.05,5)
    
    conf = {}
    conf['slots.burn.a'] = Twinfold_Bonds()+Me_and_My_Bestie()
    conf['acl'] = """
        `dragon, s=1
        `s3, not self.s3_buff
        `s4
        `s1
        `fs, x=4
        """
    coab = ['Blade', 'Marth', 'Dagger2']
    share = ['Gala_Mym']

    def prerun(self):
        if self.condition('hp60'):
            Selfbuff('a1',0.2,-1,'att','passive').on()
        else:
            Selfbuff('a1',-0.2,-1,'att','passive').on()

    def s1_proc(self, e):
        Spdbuff(e.name,0.2,10).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
