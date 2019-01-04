import adv_test
import adv
from wep.sword import flame as weapon
from core.timeline import *
from core.log import *



def module():
    return Karl

class Karl(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 3.75*2 ,
        "s1_sp"       : 2376   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.9    ,

        "s2_buff"     :[0.15, 15, 'att'] ,
        "s2_sp"       : 6610   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.1    ,

        "mod_a"   : ('att'  , 'passive' , 0.08 ) ,
        "mod_d"   : ('att'  , 'passive' , 0.6  ) ,
        "mod_wp"  : ('s'    , 'passive' , 0.25 ) ,
        "mod_wp2" : ('crit' , 'chance'  , 0.06 ) ,
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

