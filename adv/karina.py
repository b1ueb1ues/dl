import adv_test
import adv
from wep.axe import water as weapon
from core.timeline import *
from core.log import *



def module():
    return Karina

class Karina(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 2*5.43 ,
        "s1_sp"       : 3033   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.85   ,

        "s2_dmg"      : 4*2.57 ,
        "s2_sp"       : 5280   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 2.2    ,

        "mod_d"   : ('att'  , 'passive' , 0.45) ,
        "mod_d2"  : ('crit' , 'chance'  , 0.20) ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        } )
    conf.update(weapon.conf)

    def init(this):
        this.charge("prep","50%")



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `s3
        """
    adv_test.test(module(), conf, verbose=0)

