import adv_test
import adv

def module():
    return Joe

class Joe(adv.Adv):
    def init(this):
        this.dmg_make("o_burn",1.8)
        this.dmg_make("o_burn",1.8)
        this.dmg_make("o_burn",1.8)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        """
    adv_test.test(module(), conf, verbose=0)

