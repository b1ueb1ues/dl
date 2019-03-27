import adv_test
import adv

def module():
    return Musashi

class Musashi(adv.Adv):
    comment = 'poison 3 times'
    conf = {
        "mod_a3": ('att', 'killer', 0.08*0.45) ,
        } 

    def pre(this):
        if this.condition('last offense'):
            this.init = this.c_init

    def c_init(this):
        adv.Selfbuff('last_offense',0.4,15).on()
        this.dmg_make("o_s1_poison",2.65)
        this.dmg_make("o_s1_poison",2.65)
        this.dmg_make("o_s1_poison",2.65)

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

