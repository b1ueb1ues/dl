import adv_test
from adv import *
from core.timeline import *
from core.log import *
import random

from wep.dagger import water as weapon

def module():
    return Orsem

class Orsem(Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 6*1.24 ,
        "s1_sp"   : 2311   ,

        "s2_dmg"  : 4*1.59 ,
        "s2_sp"   : 4685   ,

        "mod_a"   : ('crit', 'chance', 0.10) ,
        "mod_a2"  : ('crit', 'chance', 0.06) ,

        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,
        } )
    conf.update(weapon.conf)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """

    #conf['acl'] = """
    #    `s1
    #    `s3
    #    `s2
    #    """
    adv_test.test(module(), conf, verbose=0, mass=0)

