import adv_test
import adv
from wep.sword import light as weapon
from core.timeline import *
from core.log import *



def module():
    return Raemond

class Raemond(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 3.05*2 ,
        "s1_sp"       : 2443   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.35   ,

        "s2_dmg"      : 2*3.07 ,
        "s2_sp"       : 4817   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.45   ,

        "mod_d"   : ('att'  , 'passive' , 0.60) ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,

        } )

    conf.update(weapon.conf)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s2, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

