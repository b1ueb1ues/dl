import adv_test
import adv

def module():
    return Musashi

class Musashi(adv.Adv):
    conf = {
        #"mod_a"   :  ('att'  , 'buff'     , 0.03 )  ,
        "mod_a2"  :  ('att'  , 'punisher' , 0.08*0.45 ) ,
        } 

    def init(this):
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

