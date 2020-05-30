from core.advbase import *
from slot.a import *

def module():
    return Yuya

class Yuya(Adv):
    a3 = ('primed_crit_chance', 0.5,5)
    
    conf = {}
    conf['slots.a'] = Primal_Crisis()+The_Lurker_in_the_Woods()
    conf['slots.burn.a'] = Twinfold_Bonds()+Elegant_Escort()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        if self.afflics.burn.get()
            `s1
            `fs, x=4
        else
            `fs, x=2
        end
        """
    coab = ['Blade', 'Marth', 'Grace']

    def d_coabs(self):
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Blade','Marth','Tiki']

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
