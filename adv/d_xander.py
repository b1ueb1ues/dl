import adv_test
import adv
from wep.wand import water as weapon
from core.timeline import *
from core.log import *


def module():
    return D_Xander

class D_Xander(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 4.39*2  ,
        "s1_sp"       : 2563    ,
        "s1_startup"  : 0.1     , 
        "s1_recovery" : 1.9     , 

        "s2_buff"     : [0.15, 10, 'att'] ,
        "s2_sp"       : 9609      ,
        "s2_startup"  : 0.10+0.15 , 
        "s2_recovery" : 1.05-0.15 , 

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
    conf['acl'] = acl12
    adv_test.test(module(), conf, verbose=0)


