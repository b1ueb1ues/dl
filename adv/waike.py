import adv_test
import adv

def module():
    return Waike

class Waike(adv.Adv):
    def condition(this):
        this.init = this.c_init
        this.conf['acl'] = """
            `s1, fsc
            `s2, fsc
            `s3, fsc
            `fs, seq=4
            """
        return 'bog & c4+fs'

    def init(this):
        this.bogcountlast = 0
        this.bogbuff = adv.Buff('s2_bog',0.6,8,'att','bog')


    def c_init(this):
        this.bogcountlast = 3
        this.bogbuff = adv.Buff('s2_bog',0.6,8,'att','bog')

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

