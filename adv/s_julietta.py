import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Summer_Julietta

class Summer_Julietta(Adv):
    a1 = ('affteam_bog', 0.10, 15, 5)
    a3 = ('primed_att',0.10)

    conf = {}
    conf['slots.a'] = KFM() + JotS()
    conf['acl'] = """
        `s2
        `s1
        `s3
        """
    conf['afflict_res.bog'] = 100

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
    conf = {}
    adv.adv_test.test(module(), conf)
