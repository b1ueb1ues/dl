import adv_test
import adv
from core.log import *

def module():
    return V_Orion

class V_Orion(adv.Adv):
    comment = "can not calculate burning damage"
    def init(this):
        pass
        #this.dmg_make("o_s2_burn",1.8)
        #this.dmg_make("o_s2_burn",1.8)
        #this.dmg_make("o_s2_burn",1.8)
    def h_init(this):
        log('dmg','o_s2_burn',258949.2)


    def s2_proc(this, e):
        adv.Buff("double_buff",0.08,15,wide='self').on()

    def s2_proc_vc(this, e):
        adv.Buff("double_buff",0.08,15,wide='self').on()
        adv.Buff("crown_double_buff",0.08,15,wide='self').on()

    def condition(this):
        this.conf['wp'] = ('s', 'passive', 0.25) 
        this.conf['acl'] = """
            `s1
            `s2
            `s3
            `fs, seq=3 and cancel
            """
        this.s2_proc = this.s2_proc_vc
        return 'Valiant Crown'
    

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

    module().comment = 'HMS (something just OVERPOWERED in his S1)'
    def foo(t):
        return ''
    module().condition = foo
    module().init = module().h_init
    adv_test.test(module(), conf, verbose=0)
