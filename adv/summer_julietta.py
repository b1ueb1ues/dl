from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Summer_Julietta

class Summer_Julietta(Adv):
    a1 = ('affteam_bog', 0.15, 15, 5)
    a3 = ('primed_att', 0.15)

    conf = {}
    conf['slots.a'] = Summer_Paladyns()+Primal_Crisis()
    conf['slots.frostbite.a'] = Resounding_Rendition()+His_Clever_Brother()
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3
        `s2
        `s4
        `s1
    """
    coab = ['Blade', 'Dagger', 'Summer_Estelle']
    conf['afflict_res.bog'] = 100
    share = ['Gala_Elisanne', 'Ranzal']

    def d_coabs(self):
        if self.sim_afflict:
            self.coab = ['Blade', 'Renee', 'Summer_Estelle']

    def init(self):
        self.phase['s2'] = 0
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.phase[dst] = 0
        adv.buff_class = Teambuff if adv.condition('buff all team') else Selfbuff
    
    def s1_proc(self, e):
        self.dmg_make(e.name, 6.16)
        self.afflics.bog.on(e.name, 120)
        self.dmg_make(e.name, 6.15)

    def s2_proc(self, e):
        self.phase[e.name] += 1
        self.buff_class(e.name,0.15,15).on()
        if self.phase[e.name] > 1:
            self.buff_class(e.name,0.13,15, 'crit','chance').on()
        self.phase[e.name] %= 3

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
