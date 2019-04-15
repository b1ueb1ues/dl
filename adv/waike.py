import adv_test
import adv

def module():
    return Waike

class Waike(adv.Adv):
    def pre(this):
        if this.condition('bog'):
            this.init = this.c_init

    def init(this):
        this.bogcountlast = 0
        this.bogbuff = adv.Debuff('s2_bog',-0.5,8,1,'att','bog')


    def c_init(this):
        this.bogcountlast = 3
        this.bogbuff = adv.Debuff('s2_bog',-0.5,8,1,'att','bog')
        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """

    def s2_proc(this, e):
        if this.bogcountlast > 0:
            if not this.bogbuff.get():
                this.bogcountlast -= 1
                this.bogbuff.on()



if __name__ == '__main__':
    module().comment = 'bog 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        """
    adv_test.test(module(), conf, verbose=0)

