from core.advbase import *
from module.bleed import Bleed
from slot.a import *

def module():
    return Botan

class Botan(Adv):
    a3 = [('prep',1.00), ('scharge_all', 0.05)]
    conf = {}
    conf['slots.a'] = RR() + United_by_One_Vision()
    conf['acl'] = """
        `s3, not self.s3_buff and prep
        `s2
        `s1, cancel
    """
    coab = ['Blade','Wand','Dagger']

    def d_coabs(self):
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Blade','Wand','Bow']

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff
    
    def prerun(self):
        self.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(self, e):
        Bleed(e.name, 1.46).on()

    def s2_proc(self, e):
        self.buff_class(e.name,0.1,15,'crit','chance').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)