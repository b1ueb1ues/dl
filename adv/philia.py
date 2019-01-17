import adv_test
import adv

def module():
    return Philia

class Philia(adv.Adv):
    def condition(this):
        this.conf['mod_a'] = ('att' , 'passive', 0.10)
        this.init = this.c_init
        return 'hp100 & afflic'

    def c_init(this):
        this.dmg_make("o_paralysis",1.8)
        this.dmg_make("o_paralysis",1.8)
        this.dmg_make("o_paralysis",1.8)



if __name__ == '__main__':
    module().comment = 'paralysis 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        """
    adv_test.test(module(), conf, verbose=0)
    module().comment += ' & spawn c1+fs'
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        `fs, seq=1
        """
    adv_test.test(module(), conf, verbose=0)

