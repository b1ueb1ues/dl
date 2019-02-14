import adv_test
import adv

def module():
    return V_Orion

class V_Orion(adv.Adv):

    def init(this):
        this.dmg_make("o_s2_burn",1.8)
        this.dmg_make("o_s2_burn",1.8)
        this.dmg_make("o_s2_burn",1.8)


    def s2_proc(this, e):
        adv.Buff("double_buff",0.08,15,wide='self').on()
    
def s2_proc_withcrown(this, e):
    adv.Buff("double_buff",0.08,15,wide='self').on()
    adv.Buff("crown_double_buff",0.08,15,wide='self').on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

    module().s2_proc = s2_proc_withcrown
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



