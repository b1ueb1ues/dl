import adv_test
import adv

def module():
    return Eleonora

class Eleonora(adv.Adv):

    def init(this):
        this.charge("prep",'50%')
        this.dmg_make("o_poison",2.65)
        this.dmg_make("o_poison",2.65)
        this.dmg_make("o_poison",2.65)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

