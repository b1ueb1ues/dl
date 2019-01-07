import adv_test
import adv

def module():
    return Philia

class Philia(adv.Adv):
    conf = {
        "mod_a": ('att' , 'passive' , 0.10),
        'condition':'hp100',
        } 
    def init(this):
        this.dmg_make("o_paralysis",1.8)
        this.dmg_make("o_paralysis",1.8)
        this.dmg_make("o_paralysis",1.8)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)


