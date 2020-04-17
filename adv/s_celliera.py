import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Summer_Celliera

class Summer_Celliera(Adv):
    a1 = ('bc',0.13)
    a3 = ('bt',0.30)
    conf = {}
    conf['slot.a'] = VC() + JotS()
    conf['slot.d'] = Siren()
    conf['acl'] = """
        `s2
        `s1
        `s3, fsc
        `fs, seq=2
        """
    coab = ['Blade', 'Renee', 'Summer_Estelle']
    conf['afflict_res.bog'] = 100

    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf['slot.a'] = TSO() + FRH()

    def init(self):
        self.s2_stance = 1

    def s1_proc(self, e):
        #560+168+392
        self.dmg_make('s1',1.84)
        self.afflics.bog.on('s1', 110)
        self.dmg_make('s1',5.52)

    def s2_proc(self, e):
        if self.s2_stance == 1:
            Teambuff('s2def',0.1,10,'defense').on()
            self.s2_stance = 2
        elif self.s2_stance == 2:
            Teambuff('s2def',0.1,10,'defense').on()
            Teambuff('s2atk',0.1,10).on()
            self.s2_stance = 3
        elif self.s2_stance == 3:
            Teambuff('s2def',0.1,10,'defense').on()
            Teambuff('s2atk',0.1,10).on()
            Spdbuff('s2spd',0.2,10,wide='team').on()
            self.s2_stance = 1


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
