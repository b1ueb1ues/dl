from core.advbase import *
from slot.a import *

def module():
    return Vanessa

class Vanessa(Adv):
    a1 = ('fs',0.4)
    a3 = ('lo',0.3)
    
    conf = {}
    conf['slots.a'] = Summer_Paladyns()+Primal_Crisis()
    conf['slots.burn.a'] = Resounding_Rendition()+Me_and_My_Bestie()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1, cancel
        `s2, x=4
        `s4
        `fs, x=5
    """
    coab = ['Blade', 'Marth', 'Wand']
    share = ['Ranzal']

    def d_coabs(self):
        if self.sim_afflict:
            self.coab = ['Blade','Marth','Serena']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
