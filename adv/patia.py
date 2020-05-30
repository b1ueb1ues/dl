from core.advbase import *
from module.bleed import Bleed
from slot.a import *
from slot.d import *

def module():
    return Patia

class Patia(Adv):
    a1 = ('bt',0.35)
    a3 = ('primed_crit_chance', 0.10, 5)

    conf = {}
    conf['slots.a'] = Brothers_in_Arms()+RR()
    conf['slots.d'] = Fatalis()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
        `s4
    """
    coab = ['Blade','Bow','Tobias']
    share = ['Karl']

    def prerun(self):
        self.bleed = Bleed('g_bleed',0).reset()

    def s1_proc(self, e):
        Teambuff(f'{e.name}_defense', 0.25, 15, 'defense').on()

    def s2_proc(self, e):
        Bleed(e.name, 1.46).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)