import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return D_Xainfried

class D_Xainfried(Adv):
    a1 = ('dc', 0.04)
    a3 = ('primed_att', 0.08)

    conf = {}
    conf['slots.d'] = Longlong()
    conf['slots.a'] = CC()+ADD()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3, fsc
        `fs, seq=5
        """

    def init(this):
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc

    def c_s1_proc(this, e):
        Teambuff('s1',0.2,15,'crit','chance').on()

    def s1_proc(this, e):
        Selfbuff('s1',0.2,15,'crit','chance').on()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

