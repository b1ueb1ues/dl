import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.wand import water as weapon

def module():
    return D_Xander

class D_Xander(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 4.39*2  ,
        "s1_sp"       : 2563    ,

        "s2_buff"     : [0.15, 10, 'att'] ,
        "s2_sp"       : 9609      ,

        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,
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


