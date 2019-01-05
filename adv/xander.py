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
        "s1_dmg"  : 8.25   ,
        "s1_sp"   : 2714   ,

        "s2_dmg"  : 2.48*3 ,
        "s2_sp"   : 4817   ,

        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,
        "mod_a"   : ('fs'   , 'passive' , 0.50) ,
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

