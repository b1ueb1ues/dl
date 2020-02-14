import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return S_Celliera

class S_Celliera(Adv):
    a1 = ('bc',0.13)
    a3 = ('bt',0.30)
    conf = {}
    conf['slot.a'] = VC() + JotS()
    conf['slot.d'] = DJ()
    conf['acl'] = """
        `s2
        `s1
        `s3, fsc
        `fs, seq=2
        """
    conf['afflict_res.bog'] = 100

    def d_slots(this):
        if 'wand' in this.ex:
            this.conf['slot.d'] = Siren()
        if 'bow' in this.ex:
            this.conf['slot.a'] = TSO() + FRH()

    def init(this):
        this.s2_stance = 1

    def s1_proc(this, e):
        #560+168+392
        this.dmg_make('s1',1.84)
        this.afflics.bog.on('s1', 110)
        this.dmg_make('s1',5.52)

    def s2_proc(this, e):
        if this.s2_stance == 1:
            Teambuff('s2def',0.0,10).on()
            Event('defchain').on()
            this.s2_stance = 2
        elif this.s2_stance == 2:
            Teambuff('s2def',0.0,10).on()
            Teambuff('s2atk',0.1,10).on()
            Event('defchain').on()
            this.s2_stance = 3
        elif this.s2_stance == 3:
            Teambuff('s2def',0.0,10).on()
            Teambuff('s2atk',0.1,10).on()
            Spdbuff('s2spd',0.2,10,wide='team').on()
            Event('defchain').on()
            this.s2_stance = 1


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)
