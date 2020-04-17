from core.advbase import *
from module.bleed import Bleed
from slot.d import *
from slot.a import *

def module():
    return Patia

class Patia(Adv):
    a1 = ('bt',0.35)
    a3 = ('primed_crit_chance', 0.10, 5)

    conf = {}
    conf['slots.d'] = Fatalis()
    conf['slots.a'] = Resounding_Rendition()+Brothers_in_Arms()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
    """

    def prerun(self):
        self.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(self, e):
        Teambuff('s1', 0.25, 15, 'defense').on()
        #Teambuff('s1',0.10,9.375).on()

    def s2_proc(self, e):
        Bleed("s2", 1.46).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)