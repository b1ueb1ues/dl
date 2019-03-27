import adv_test
import adv

def module():
    return Philia

class Philia(adv.Adv):
    conf = {}
    conf['mod_a1'] = ('att', 'passive', 0.10, 'hp100')
    def pre(this):
        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """

    def init(this):
        this.dmg_make("o_s2_paralysis",1.8)
        this.dmg_make("o_s2_paralysis",1.8)
        this.dmg_make("o_s2_paralysis",1.8)



if __name__ == '__main__':
    module().comment = 'paralysis 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        """
    adv_test.test(module(), conf, verbose=0)

