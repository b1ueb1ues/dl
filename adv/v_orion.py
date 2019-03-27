import adv_test
import adv
from core.log import *

def module():
    return V_Orion

class V_Orion(adv.Adv):
    def init(this):
        this.dmg_make("o_s2_burn",0.803*3)
        this.dmg_make("o_s2_burn",0.803*3)
        this.dmg_make("o_s2_burn",0.803*3)

    def s2_proc(this, e):
        adv.Selfbuff("double_buff",0.08,15).on()

    def s2_proc_vc(this, e):
        adv.Selfbuff("double_buff",0.08,15).on()
        adv.Selfbuff("crown_double_buff",0.08,15).on()

    def pre(this):
        if this.condition('Valiant Crown'):
            this.conf['mod_wp'] = [('s', 'passive', 0.25)]
            this.conf['acl'] = """
                `s1
                `s2
                `s3
                `fs, seq=3 and cancel
                """
            this.s2_proc = this.s2_proc_vc
    

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

