import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return S_Celliera

class S_Celliera(Adv):
    comment = 'no bog'
    conf = {}
    conf['slot.a'] = TSO() + JotS()
    #conf['slot.d'] = DJ()

    a1 = ('bc',0.13)
    a3 = ('bt',0.30)

    def init(this):
        this.s2_stance = 1
        this.spdbuff = Teambuff('s2spd',0.2,10)


    def speed(this):
        return this.spdbuff.stack()*0.2 + 1

    def s2_proc(this, e):
        if this.s2_stance == 1:
            Teambuff('s2def',0.0,10).on()
            Event('defchain').on()
            this.s2_stance = 2
        elif this.s2_stance == 2:
            Teambuff('s2def',0.0,10).on()
            Teambuff('s2atk',0.1,10).on()
            this.s2_stance = 3
        elif this.s2_stance == 3:
            Teambuff('s2def',0.0,10).on()
            Teambuff('s2atk',0.1,10).on()
            Teambuff('s2spd',0.2,10,'att','spd').on()
            this.s2_stance = 1


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1,fsc
        `s2,fsc
        `s3,fsc
        `fs, x=3
        """
    adv_test.test(module(), conf, verbose=-2)
