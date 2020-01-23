import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return W_Elisanne


class W_Elisanne(Adv):
    comment = '2in1'
    
    conf = {}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = TSO()+FRH()
        else:
            this.conf.slot.a = TSO()+JotS()

    a1 = ('sp',0.08)
    a3 = ('bc',0.13)

    def prerun(this):
        this.s2debuff = Debuff('s2defdown',0.15,10,1)
        if this.condition('s2 defdown for 10s'):
            this.s2defdown = 1
        else:
            this.s2defdown = 1

    def s2_proc(this, e):
        if this.s2defdown :
            this.s2debuff.on()

if __name__ == '__main__':
    conf = {}
    #conf['slot.d'] = Garland()
    conf['acl'] = """
        `rotation
    """
    conf['rotation_init'] = """
        c3fsc3fsc3fss1
        c3fsc3fsc2fsc2fs
    """
    conf['rotation'] = """
        s2c2fss1
        c3fsc3fsc3fss1
        c2fss3c3fsc3fs
        s2c2fss1
        c3fsc3fsc3fss1
        c2fsc3fsc3fs
    """
    adv_test.test(module(), conf, verbose=-2, mass=0)
