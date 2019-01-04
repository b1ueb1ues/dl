import adv_test
import adv
from wep.blade import water as weapon
from core.timeline import *
from core.log import *



def module():
    return Jurota

class Jurota(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 8.78   ,
        "s1_sp"       : 2630   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.9    ,

        "s2_buff"     : [0.25, 5, 'att'] ,
        "s2_sp"       : 4101   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.1    ,

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

