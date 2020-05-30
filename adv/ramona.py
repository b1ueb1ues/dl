from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Ramona

class Ramona(Adv):
    a1 = ('primed_att',0.10)
    a3 = ('bc',0.13)
    conf = {}
    conf['slots.a'] = Summer_Paladyns()+Primal_Crisis()
    conf['slots.burn.a'] = Resounding_Rendition()+Elegant_Escort()
    conf['acl'] = """
        `dragon, s=1
        `s3, not self.s3_buff
        `s1
        `s2,x=4
        """
    coab = ['Blade', 'Wand', 'Marth']

    def prerun(self):
        self.a_s1 = self.s1.ac
        self.a_s1a = S('s1', Conf({'startup': 0.10, 'recovery': 3.10}))
        def recovery():
            return self.a_s1a._recovery + self.a_s1.getrecovery()
        self.a_s1a.getrecovery = recovery
        self.s1.ac = self.a_s1a

    def s1_proc(self, e):
        self.dmg_make(e.name, 2.93*6)
        self.hits += 6

    def s2_proc(self, e):
       Event('defchain')()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)