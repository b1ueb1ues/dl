import adv_test
import adv
from wep.blade import water as weapon
from core.timeline import *
from core.log import *


def module():
    return Celliera

class Celliera(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 2.42*4  ,
        "s1_sp"       : 2537    ,
        "s1_startup"  : 0.1     , #108/60
        "s1_recovery" : 1.8     , #108/60

        "s2_buff"     : [0.25, 10, 'att'] ,
        "s2_sp"       : 4877      ,
        "s2_startup"  : 0.10+0.15 , 
        "s2_recovery" : 1.05-0.15 , #65/60

        "mod_a"   : ('att'  , 'passive' , 0.08)  ,
        "mod_d"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        } )
    conf.update(weapon.conf)



if __name__ == '__main__':
    conf = {}
    acl12 = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    acl21 = """
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5
        """ 
    # test that 12 is better than 21
    if 1:
        conf['acl'] = acl12
        adv_test.test(module(), conf, verbose=0)
        exit()

    conf['acl'] = acl21
    adv_test.test(module(), conf, verbose=0)


