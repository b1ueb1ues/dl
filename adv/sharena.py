from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Sharena

class Sharena(Adv):
    comment = 'fs guard not considered'
    a1 = ('lo_crit_chance', 1.00, 10)
    a3 = ('k_paralysis',0.30)

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon, fsc
        `s1
        `s2, cancel
        `fs, x=5
    """
    coab = ['Malora','Dagger','Peony']
    conf['afflict_res.paralysis'] = 0

    def d_coabs(self):
        if self.duration <= 60:
            self.coab = ['Blade','Dagger','Peony']

    def prerun(self):
        self.s2_debuff = Debuff('s2',0.05,10)
        # Teambuff('fs_guard',0.15,-1,'att').on()

    def s1_proc(self, e):
        self.afflics.paralysis(e.name,120, 0.97)

    def s2_proc(self, e):
        self.s2_debuff.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
