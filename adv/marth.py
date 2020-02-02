import adv_test
import adv
from adv import *
from slot.d import *
from slot.a import *

def module():
    return Marth

class Marth(adv.Adv):
    comment = 'c2fs'
    a1 = ('prep',100)
    a3 = ('cc',0.13,'hit15')
    conf = {}
    conf['slot.a'] = TSO()+Primal_Crisis()
    #conf['slot.d'] = Cerberus()

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
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s2
        `s1,fsc
        `fs, seq=2
        """
#    import slot
#    conf['slots.d'] = slot.d.flame.Sakuya()

    adv_test.test(module(), conf, verbose=-2)
