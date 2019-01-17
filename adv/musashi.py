import adv_test
import adv

def module():
    return Musashi

class Musashi(adv.Adv):
    comment = 'poison 3 times'
    conf = {
        "mod_a"  :  ('att'  , 'punisher' , 0.08*0.45 ) ,
        } 

    def condition(this):
        this.init = this.c_init
        return 'afflic & last offense'

    def c_init(this):
        adv.Buff('last_offense',0.4,15,wide='self').on()
        this.dmg_make("o_poison",2.65)
        this.dmg_make("o_poison",2.65)
        this.dmg_make("o_poison",2.65)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 
        `s1
        `s3, s
        """
    adv_test.test(module(), conf, verbose=1)

