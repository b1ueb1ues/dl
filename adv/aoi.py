import adv_test
import adv
import wep.blade
from core.timeline import *
from core.log import *



def module():
    return Aoi

class Aoi(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 8.78   ,
        "s1_sp"   : 2630   ,
        "s1_time" : 1.9    ,

        "s2_dmg"  : 7.90   ,
        "s2_sp"   : 5280   ,
        "s2_time" : 1.9    ,

        "s3_dmg"  : 3.54*3 ,
        "s3_sp"   : 8030   ,
        "s3_time" : 2.7    ,
        } )
    conf.update(wep.blade.conf)

    def init(this):
        pass
    
    def sp_mod(this, name):
        return 1

    def att_mod(this):
        return 1.6

    def dmg_mod_x(this, name):
        return 1

    def dmg_mod_s(this, name):
        return 1.25






if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

