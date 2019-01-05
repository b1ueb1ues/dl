import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.blade import wind as weapon

def module():
    return Musashi

class Musashi(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 4.32*2 ,
        "s1_sp"       : 2567   ,

        "s2_buff"     : [0.3, 5, 'att'] ,
        "s2_sp"       : 4430   ,

        "mod_a"   :  ('att'  , 'buff'     , 0.03 )  ,
        "mod_a2"  :  ('att'  , 'punisher' , 0.08*0.45 ) ,
        } )
    conf.update(weapon.conf)

    def init(this):
        this.dmg_make("o_poison",2.65)
        this.dmg_make("o_poison",2.65)
        this.dmg_make("o_poison",2.65)




if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5 
        `s3, s
        """
    adv_test.test(module(), conf, verbose=0)

