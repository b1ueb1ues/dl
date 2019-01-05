import adv_test
from adv import *
from core.timeline import *
from core.log import *
import random

from wep.dagger import flame as weapon

def module():
    return Renelle

class Renelle(Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 3*2.26 ,
        "s1_sp"   : 2318   ,

        "s2_dmg"  : 2*2.88 ,
        "s2_sp"   : 4892   ,

        "mod_a"   : ('crit', 'chance', 0.08) ,
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

