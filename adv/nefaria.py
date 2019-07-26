import adv_test
import adv

def module():
    return Nefaria

class Nefaria(adv.Adv):
    def c_prerun(this):
        this.dmg_make("o_s1hitblind",(1.8444*1.3-1.06)*8)
        this.dmg_make("o_s1hitblind",(1.8444*1.3-1.06)*8)
        this.dmg_make("o_s1hitblind",(1.8444*1.3-1.06)*8)
        adv.Selfbuff('blindpunisher',0.3,20,'att','killer').on()
        this.o_prerun()

        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """


    def prerun(this):
        this.s2fscharge = 0


    def s2_proc(this, e):
        this.s2fscharge = 3

    def fs_proc(this, e):
        if this.s2fscharge > 0:
            this.s2fscharge -= 1
            this.dmg_make("o_s2fs",0.48)

    def init(this):
        if this.condition('blind 20s (s1 boosted 3times)'):
            this.prerun, this.o_prerun = this.c_prerun, this.prerun


if __name__ == '__main__':
    module().comment = 'boost dmg from blind 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

