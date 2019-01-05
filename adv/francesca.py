import adv_test
from adv import *
from core.timeline import *
from core.log import *
import random

from wep.dagger import wind as weapon

def module():
    return Francesca

class Francesca(Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 4*1.69 ,
        "s1_sp"   : 2257   ,

        "s2_dmg"  : 2*2.88 ,
        "s2_sp"   : 4892   ,

        "mod_fs"  : ('fs', 'passive', 0.30) ,
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

