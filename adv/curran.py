import adv_test
import adv

def module():
    return Curran

class Curran(adv.Adv):
    comment = "do not use weapon skill and fs"
    conf = {
        "mod_a": ('att', 'bane', 0.13*0.45),
        } 
    def condition(this):
        this.init = this.c_init
        return 'last offense'

    def c_init(this):
        adv.Buff('last_offense',0.5,15,wide='self').on()

    def s1_proc(this, e):
        adv.Buff('defdown',-0.025,10,'def').on()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        """
    adv_test.test(module(), conf, verbose=0)

