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
        self.s2_stance = 1
        if self.condition('buff all team'):
            self.s2_proc = self.c_s2_proc

    def s1_proc(self, e):
        #560+168+392
        self.dmg_make('s1',5.60)
        self.afflics.bog.on('s1', 110)
        self.dmg_make('s1',5.60)

    def s2_proc(self, e):
        if self.s2_stance == 1:
            Selfbuff('s2',0.15,15).on()
            self.s2_stance = 2
        elif self.s2_stance == 2:
            Selfbuff('s2',0.15,15).on()
            Selfbuff('s2',0.10,15, 'crit','chance').on()
            self.s2_stance = 3
        elif self.s2_stance == 3:
            Selfbuff('s2',0.15,15).on()
            Selfbuff('s2',0.10,15, 'crit','chance').on()
            self.s2_stance = 1

    def c_s2_proc(self, e):
        if self.s2_stance == 1:
            Teambuff('s2',0.15,15).on()
            self.s2_stance = 2
        elif self.s2_stance == 2:
            Teambuff('s2',0.15,15).on()
            Teambuff('s2',0.10,15, 'crit','chance').on()
            self.s2_stance = 3
        elif self.s2_stance == 3:
            Teambuff('s2',0.15,15).on()
            Teambuff('s2',0.10,15, 'crit','chance').on()
            self.s2_stance = 1

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)