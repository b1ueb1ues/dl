import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.sword import shadow as weapon

def module():
    return Rodrigo

class Rodrigo(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 6.82   ,
        "s1_sp"       : 2613   ,

        "s2_dmg"      : 6.14   ,
        "s2_sp"       : 4886   ,

        "mod_a"   : ('att'  , 'passive' , 0.08) ,
        } )

    conf.update(weapon.conf)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

