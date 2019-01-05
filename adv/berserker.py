import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.sword import shadow as weapon


def module():
    return Berserker

class Berserker(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg" : 3.35*2 ,
        "s1_sp"  : 2376   ,

        "s2_dmg" : 0      ,
        "s2_sp"  : 5750   ,

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

