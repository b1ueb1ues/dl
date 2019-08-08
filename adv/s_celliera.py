if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

from adv import *
from slot.a import *
from slot.d import *

def module():
    return S_Celliera

class S_Celliera(Adv):
    comment = 'no bog; don\'t s3; c2fs'
    a1 = ('bc',0.13)
    a3 = ('bt',0.30)
    conf = {}
    #conf['slot.a'] = TSO() + JotS()
    conf['slot.a'] = VC() + JotS()
    conf['slot.d'] = DJ()
    conf['acl'] = """
        `s2
        `s1
        `fs, x=2
        """

    def d_slots(this):
        if 'wand' in this.ex:
            this.conf['slot.d'] = Siren()


    def init(this):
        this.s2_stance = 1


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
    adv_test.test(module(), conf, verbose=-2)
