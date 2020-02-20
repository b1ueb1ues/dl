import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Marth

class Marth(Adv):
    comment = 'c2fs'
    a1 = ('prep',100)
    a3 = ('cc',0.13,'hit15')
    conf = {}
    conf['slot.a'] = Mega_Friends()+Primal_Crisis()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s2,fsc
        `s1,fsc
        `fs, seq=2
        """

    def init(this):
        this.stance = 0

    def s2_proc(this, e):
        if this.stance == 0:
            this.stance = 1
            Selfbuff('s21',0.1,10).on()
        elif this.stance == 1:
            this.stance = 2
            Teambuff('s22',0.1,10).on()
        elif this.stance == 2:
            this.stance = 0
            Teambuff('s23',0.1,10).on()
            Spdbuff('s23s',0.3,10, wide='team').on()




if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
