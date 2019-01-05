import adv_test
from adv import *
from core.timeline import *
from core.log import *
import random

from wep.dagger import shadow as weapon

def module():
    return Orion

class Orion(Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 4*1.59 ,
        "s1_sp"   : 2213   ,

        "s2_dmg"  : 4*1.67 ,
        "s2_sp"   : 4904   ,

        "mod_a"   : ('crit', 'chance', 0.10)
        } )
    conf.update(weapon.conf)

    def init(this):
        this.charge('prep','50%')


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

