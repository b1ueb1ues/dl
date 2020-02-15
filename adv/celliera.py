import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *


def module():
    return Celliera

class Celliera(Adv):
    a3 = ('a',0.08,'hp70')

    conf = {}
    conf['slots.a'] = RR()+JotS()
    #conf['slots.d'] = DJ()
    acl12 = """
        `s1
        `s2, seq=5
        `s3
        """
    acl21 = """
        `s2, seq=5
        `s1
        `s3
        """ 
    conf['acl'] = acl21
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = RR()+BN()

    def prerun(this):
        this.s2buff = adv.Selfbuff("s2_shapshifts1",1, 10,'ss','ss')
        this.s2str = adv.Selfbuff("s2_str",0.25,10)



    def s1_proc(this, e):
        if this.s2buff.get():
            this.s2buff.buff_end_timer.timing += 2.5
            this.s2str.buff_end_timer.timing += 2.5

    def s2_proc(this, e):
        this.s2buff.on()
        this.s2str.on()



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)


