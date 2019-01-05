import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.blade import flame as weapon

def module():
    return Aoi

class Aoi(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg" : 8.78   ,
        "s1_sp"  : 2630   ,

        "s2_dmg" : 7.90   ,
        "s2_sp"  : 5280   ,

        "mod_a"  : ('att' , 'punisher' , 0.04) ,
        } )
    conf.update(weapon.conf)

    def init(this):
        pass
    



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

