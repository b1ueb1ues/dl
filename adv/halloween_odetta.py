from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Halloween_Odetta

class Halloween_Odetta(Adv):
    a1 = ('primed_defense', 0.10)
    a3 = ('bt',0.2)

    conf = {}
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act('c3 s end'), s=2
        `s2, cancel
        `s1, fsc
        `fs, x=3 and not self.afflics.frostbite.get()
        `fs, x=2 and self.afflics.frostbite.get()
    """
    coab = ['Summer_Estelle','Blade','Dagger']

    def d_coabs(self):
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Summer_Estelle','Blade','Renee']

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.buff_class = Teambuff if adv.condition('buff all team') else Selfbuff

    def s2_proc(self, e):
        self.buff_class(e.name,0.2,15).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)