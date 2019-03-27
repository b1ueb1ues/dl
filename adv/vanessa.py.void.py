import adv_test
import adv
import vanessa

def module():
    return Vanessa

class Vanessa(vanessa.Vanessa):
    comment = 'void weapon vs HMS'

    def pre(this):
        this.conf['str_w'] = 1.5*380
        this.conf['mod_w'] = ('att','killer',0.2)
        if this.condition('last offense'):
            this.o_init = this.init
            this.init = this.c_init
    
    def init(this):
        this.charge_p('prep','50%')

    def c_init(this):
        this.o_init()
        adv.Selfbuff('last_offense',0.3,15).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

