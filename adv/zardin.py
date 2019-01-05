import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.sword import water as weapon

def module():
    return Zardin

class Zardin(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 6.82   ,
        "s1_sp"   : 2443   ,

        "s2_dmg"  : 5.52   ,
        "s2_sp"   : 5225   ,

        "mod_a"   : ('att'  , 'passive' , 0.10)  ,
        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,
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

