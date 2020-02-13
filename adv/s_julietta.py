import adv.adv_test
from adv import *
from slot.a import *

def module():
    return S_Julietta

class S_Julietta(Adv):
    a3 = ('primed_att',0.10)

    conf = {}
    conf['slot.a'] = KFM() + JotS()
    conf['acl'] = """
        `s2
        `s1
        `s3
        """
    conf['afflict_res.bog'] = 100

    def init(this):
        this.s2_stance = 1
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc

    def s1_proc(this, e):
        #560+168+392
        this.dmg_make('s1',5.60)
        this.afflics.bog.on('s1', 110)
        this.dmg_make('s1',5.60)

    def s2_proc(this, e):
        if this.s2_stance == 1:
            Selfbuff('s2',0.15,15).on()
            this.s2_stance = 2
        elif this.s2_stance == 2:
            Selfbuff('s2',0.15,15).on()
            Selfbuff('s2',0.10,15, 'crit','chance').on()
            this.s2_stance = 3
        elif this.s2_stance == 3:
            Selfbuff('s2',0.15,15).on()
            Selfbuff('s2',0.10,15, 'crit','chance').on()
            this.s2_stance = 1

    def c_s2_proc(this, e):
        if this.s2_stance == 1:
            Teambuff('s2',0.15,15).on()
            this.s2_stance = 2
        elif this.s2_stance == 2:
            Teambuff('s2',0.15,15).on()
            Teambuff('s2',0.10,15, 'crit','chance').on()
            this.s2_stance = 3
        elif this.s2_stance == 3:
            Teambuff('s2',0.15,15).on()
            Teambuff('s2',0.10,15, 'crit','chance').on()
            this.s2_stance = 1

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
