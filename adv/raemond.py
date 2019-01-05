import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.sword import light as weapon


def module():
    return Raemond

class Raemond(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 3.05*2 ,
        "s1_sp"       : 2443   ,

        "s2_dmg"      : 2*3.07 ,
        "s2_sp"       : 4817   ,
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

