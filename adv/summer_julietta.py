from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Summer_Julietta

class Summer_Julietta(Adv):
    a1 = ('affteam_bog', 0.10, 15, 5)
    a3 = ('primed_att',0.10)

    conf = {}
    conf['slots.a'] = Summer_Paladyns()+Primal_Crisis()
    conf['slots.frostbite.a'] = Resounding_Rendition()+His_Clever_Brother()
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s2
        `s1
        `s3
    """
    coab = ['Blade', 'Dagger', 'Summer_Estelle']
    conf['afflict_res.bog'] = 100

    def d_coabs(self):
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Blade', 'Renee', 'Summer_Estelle']

    def init(self):
        self.phase['s2'] = 0
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.phase[dst] = 0
        adv.buff_class = Teambuff if adv.condition('buff all team') else Selfbuff
    
    def s1_proc(self, e):
        #560+168+392
        self.dmg_make(e.name,5.60)
        self.afflics.bog.on(e.name, 110)
        self.dmg_make(e.name,5.60)

    def s2_proc(self, e):
        self.phase[e.name] += 1
        self.buff_class(e.name,0.15,15).on()
        if self.phase[e.name] > 1:
            self.buff_class(e.name,0.10,15, 'crit','chance').on()
        self.phase[e.name] %= 3

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
