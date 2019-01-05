import adv_test
from adv import *
from core.timeline import *
from core.log import *
import random

from wep.dagger import water as weapon

def module():
    return Luther

class Luther(Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 4*1.86 ,
        "s1_sp"   : 2343   ,

        "s2_dmg"  : 4*1.44 ,
        "s2_sp"   : 4904   ,

        "mod_a"   : ('crit', 'chance', 0.10) ,
        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,
        } )
    conf.update(weapon.conf)

    def s2_proc(this, e):
        Buff('s2_ab',-0.015,10,'def').on()



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

