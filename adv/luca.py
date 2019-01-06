import adv_test
import adv

def module():
    return Luca

class Luca(adv.Adv):
    conf = {
        "mod_a" : ('att' , 'passive' , 0.13)  ,
        'condition':'hp100',
        } 

    def init(this):
        this.dmg_make("o_paralysis",2.65)
        this.dmg_make("o_paralysis",2.65)
        this.dmg_make("o_paralysis",2.65)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5
        """

    adv_test.test(module(), conf, verbose=0)

