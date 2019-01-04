import adv_test
import adv
from wep.blade import shadow as weapon
from core.timeline import *
from core.log import *



def module():
    return Taro

class Taro(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 2.93*3 ,
        "s1_sp"       : 2392   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 2.8    ,

        "s2_dmg"      : 7.9    ,
        "s2_sp"       : 5259   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.95   ,

        "mod_d"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        } )
    conf.update(weapon.conf)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

