import adv_test
import adv

def module():
    return Vanessa

class Vanessa(adv.Adv):
    comment = 'void weapon vs HMS'
    conf = {
        "mod_a": ('fs', 'passive', 0.40),
        } 
    conf['str_w'] = 1.5*380
    conf['mod_w'] = ('att','punisher',0.2)

    def pre(this):
        if this.condition('last offense'):
            this.o_init = this.init
            this.init = this.c_init
    
    def init(this):
        this.charge_p('prep','50%')

    def c_init(this):
        this.o_init()
        adv.Buff('last_offense',0.3,15,wide='self').on()


    def s2_proc(this, e):
        adv.Buff('defdown',-0.05,10,'def').on()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

