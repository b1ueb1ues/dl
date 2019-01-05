import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.blade import shadow as weapon

def module():
    return Taro

class Taro(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 2.93*3 ,
        "s1_sp"       : 2392   ,

        "s2_dmg"      : 7.9    ,
        "s2_sp"       : 5259   ,
        } )
    conf.update(weapon.conf)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

