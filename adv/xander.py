import adv_test
import adv
from wep.sword import water as weapon
from core.timeline import *
from core.log import *



def module():
    return Xander

class Xander(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 8.25   ,
        "s1_sp"       : 2714   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.9    ,

        "s2_dmg"      : 2.48*3   ,
        "s2_sp"       : 4817   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.9    ,

        "mod_p"   : ('fs'   , 'passive' , 0.50) ,
        "mod_d"   : ('att'  , 'passive' , 0.45) ,
        "mod_d2"  : ('crit' , 'chance'  , 0.20) ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        #"mod_wp3" : ('fs'   , 'passive' , 0.20) ,
        #"mod_wp4" : ('s'    , 'passive' , 0.10) ,
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

