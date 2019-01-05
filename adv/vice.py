import adv_test
from adv import *
from core.timeline import *
from core.log import *
import random

from wep.dagger import shadow as weapon

def module():
    return Vice

class Vice(Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 4*1.69 ,
        "s1_sp"   : 2257   ,

        "s2_dmg"  : 2*2.88 ,
        "s2_sp"   : 4892   ,

        "mod_a"   : ('att', 'bp', 0.2*0.15)
        } )
    conf.update(weapon.conf)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

