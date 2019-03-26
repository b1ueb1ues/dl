import adv_test
import adv

def module():
    return Jakob

class Jakob(adv.Adv):
    def pre(this):
        if this.condition('bog'):
            this.o_init = this.init
            this.init = this.c_init

    def init(this):
        this.charge_p('prep','50%')
        this.bogcountlast = 0
        this.bogbuff = adv.Buff('s1_bog',0.5,8,'att','bog')


    def c_init(this):
        this.bogcountlast = 3
        this.bogbuff = adv.Buff('s1_bog',0.5,8,'att','bog')

    def s1_proc(this, e):
        if this.bogcountlast > 0:
            if not this.bogbuff.get():
                this.bogcountlast -= 1
                this.bogbuff.on()



if __name__ == '__main__':
    module().comment = 'bog 3 times'
    conf = {}
    conf['acl'] = """
        `s1
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

