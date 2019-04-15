import adv_test
import adv

def module():
    return Musashi

class Musashi(adv.Adv):
    comment = 'poison 3 times'
    a1 = ('lo',0.40)
    a3 = ('od',0.08)

    def init(this):
        this.dmg_make("o_s1_poison",2.65)
        this.dmg_make("o_s1_poison",2.65)
        this.dmg_make("o_s1_poison",2.65)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 
        `s1
        `s3, s
        """
    adv_test.test(module(), conf, verbose=0)

