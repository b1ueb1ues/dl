import adv_test
import adv

def module():
    return Eleonora

class Eleonora(adv.Adv):
    def init(this):
        this.charge("prep",'50%')
        this.dmg_make("o_s1_poison",2.65)
        this.dmg_make("o_s1_poison",2.65)
        this.dmg_make("o_s1_poison",2.65)
    def condition(this):
        this.conf['acl'] = """
            `s1, fsc
            `s2, fsc
            `s3, fsc
            `fs, seq=4
            """
        return 'c4+fs'



if __name__ == '__main__':
    module().comment = 'poison by s1 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5 
        """
    adv_test.test(module(), conf, verbose=0)
