import adv_test
import adv

def module():
    return Nefaria

class Nefaria(adv.Adv):
    def init(this):
        this.dmg_make("o_s1hitblind",7.3352*1.3-1.06)
        this.dmg_make("o_s1hitblind",7.3352*1.3-1.06)
        this.dmg_make("o_s1hitblind",7.3352*1.3-1.06)
        this.s2fscharge = 0

    def s2_proc(this, e):
        this.s2fscharge = 3

    def fs_proc(this, e):
        if this.s2fscharge > 0:
            this.s2fscharge -= 1
            this.dmg_make("o_s2fs",0.48)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s3, seq=5 or fsc
        """
    adv_test.test(module(), conf, verbose=0)
    module().comment = 'spawn c1+fs'
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        `fs, seq=1
        """
    adv_test.test(module(), conf, verbose=0)

