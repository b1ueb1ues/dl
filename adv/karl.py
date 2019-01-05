import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.sword import flame as weapon


def module():
    return Karl

class Karl(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 3.75*2 ,
        "s1_sp"   : 2376   ,

        "s2_buff" :[0.15, 15, 'att'] ,
        "s2_sp"   : 6610   ,

        "mod_a"   : ('att'  , 'passive' , 0.08 ) ,
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

