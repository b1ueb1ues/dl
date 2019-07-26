import adv_test
import adv

def module():
    return Jakob

class Jakob(adv.Adv):
    def init(this):
        if this.condition('bog<=3'):
            this.o_prerun = this.prerun
            this.prerun = this.c_prerun

    def prerun(this):
        this.charge_p('prep','50%')
        this.bogcountlast = 0
        this.bogbuff = adv.Debuff('s1_bog',-0.5,8,1,'att','bog')


    def c_prerun(this):
        this.bogcountlast = 3
        this.bogbuff = adv.Debuff('s1_bog',-0.5,8,1,'att','bog')

    def s1_proc(this, e):
        if this.bogcountlast > 0:
            if not this.bogbuff.get():
                this.bogcountlast -= 1
                this.bogbuff.on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

