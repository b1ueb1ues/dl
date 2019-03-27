import adv_test
import adv

def module():
    return Hawk

class Hawk(adv.Adv):
    def init(this):
        this.s2fscharge = 0

    def c_init(this):
        this.dmg_make("o_s1hitstun",18.232*1.3-8.48)
        this.dmg_make("o_s1hitstun",18.232*1.3-8.48)
        this.dmg_make("o_s1hitstun",18.232*1.3-8.48)
        adv.Selfbuff('stunpunisher',0.3,20,'att','killer').on()
        this.o_init()

    def pre(this):
        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """
        if this.condition('stun 20s(3 s1 boosted)'):
            this.init, this.o_init = this.c_init, this.init

    def s2_proc(this, e):
        this.s2fscharge = 3

    def fs_proc(this, e):
        if this.s2fscharge > 0:
            this.s2fscharge -= 1
            this.dmg_make("o_s2fs",0.48)


if __name__ == '__main__':
    #module().comment = 'boost dmg from stun 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

