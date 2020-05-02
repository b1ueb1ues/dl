from core.advbase import *
from slot.a import *

def module():
    return Vanessa

class Vanessa(Adv):
    a1 = ('fs',0.4)
    a3 = ('lo',0.3)
    
    conf = {}
    conf['slots.a'] = Summer_Paladyns()+Primal_Crisis()
    conf['slots.burn.a'] = Resounding_Rendition()+Elegant_Escort()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1, cancel
        `s2, x=4
        `fs, x=5
    """
    coab = ['Blade', 'Marth', 'Wand']

    def d_coabs(self):
#        if self.duration <= 120 and self.duration > 60:
#            self.coab = ['Blade', 'Marth', 'Hmym']
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Blade','Marth','Serena']

#    def d_slots(self):
#        if self.duration <= 120 and self.duration > 60:
#            self.conf['slots.a'] = Resounding_Rendition() + Breakfast_at_Valerios()
#   Websim gives better results for this than Bash

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
