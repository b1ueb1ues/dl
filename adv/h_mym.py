import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return H_Mym

class H_Mym(Adv):
    a1 = ('cd',0.3)

    conf = {}
    conf['slots.a'] = KFM()+JotS()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1
        `s2, x=5 or fsc
        `fs, x=5
    """

    def prerun(this):
        if this.condition('s1 defdown for 10s'):
            this.s1defdown = 1
        else:
            this.s1defdown = 0
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc

    def init(this):
        this.slots.c.ex = {'hmym':('ex', 'hmym')}

    def s1_proc(this, e):
        if this.s1defdown :
            Debuff('s1defdown',0.15,10,1).on()
    
    def c_s2_proc(this, e):
        Teambuff('s2',0.20,15).on()
        Selfbuff('s2_dreamboost',0.05,15,'crit','rate').on()

    def s2_proc(this, e):
        Selfbuff('s2',0.20,15).on()
        Selfbuff('s2_dreamboost',0.05,15,'crit','rate').on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2, mass=0)
