import adv_test
from v_orion import *
import adv

def module():
    return V_Orion_vc

class V_Orion_vc(V_Orion):
    adv_name = 'V_Orion'

    def s2_proc(this, e):
        adv.Selfbuff("double_buff",0.08,15).on()
        adv.Selfbuff("crown_double_buff",0.08,15).on()
    

if __name__ == '__main__':
    conf = {}
    module().comment = 'Valiant Crown'
    conf['acl'] = """
        `s1, sp
        `s2, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    conf.update({
        "mod_wp"  : ('s'   , 'passive' , 0.25) ,
        })
    adv_test.test(module(), conf, verbose=0)



