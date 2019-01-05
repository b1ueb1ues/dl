import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.wand import flame as weapon

def module():
    return Xania

class Xania(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 8.85 ,
        "s1_sp"       : 2759 ,

        "s2_dmg"      : 8.05 ,
        "s2_sp"       : 5570 ,

        "mod_a"   : ("s"    , 'passive' , 0.20) ,
        } )
    conf.update(weapon.conf)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

