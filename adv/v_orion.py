import adv_test
import adv
from core.log import *
from slot.a import *

def module():
    return V_Orion

class V_Orion(adv.Adv):
    def init(this):
        this.dmg_make("o_s2_burn",0.803*3)
        this.dmg_make("o_s2_burn",0.803*3)
        this.dmg_make("o_s2_burn",0.803*3)
        this.dc_event = Event('defchain')

    def c_init(this):
        this.conf['acl'] = """
            `s1
            `s2
            `s3
            `fs, seq=3 and cancel
            """
        this.o_init()

    def s2_proc(this, e):
        adv.Selfbuff("double_buff",0.08,15).on()
        this.dc_event()

    def s2_proc_vc(this, e):
        adv.Selfbuff("double_buff",0.08,15).on()
        this.dc_event()
        #Event('defchain')()
        #adv.Selfbuff("crown_double_buff",0.08,15).on()

    def pre(this):
        if this.condition('VC+RR'):
            this.conf['slots.a'] = VC()+RR()
            #this.s2_proc = this.s2_proc_vc
            this.init,this.o_init = this.c_init, this.init
    

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

