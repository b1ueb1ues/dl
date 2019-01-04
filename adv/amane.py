import adv_test
import adv
from wep.wand import light as weapon
from core.timeline import *
from core.log import *


def module():
    return Amane

class Amane(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 4.92*2  ,
        "s1_sp"       : 2711    ,
        "s1_startup"  : 0.1     , #108/60
        "s1_recovery" : 1.8     , #108/60

        "s2_buff"     : [0.15, 10, 'att'] ,
        "s2_dmg"      : 0         ,
        "s2_sp"       : 11449     ,
        "s2_startup"  : 0.10+0.15 , #65/60
        "s2_recovery" : 1.05-0.15 , #65/60

        "mod_d"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        } )
    conf.update(weapon.conf)

    def init(this):
        this.charge("prep","75%")



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
    # test that 21 is better than 12
    # s3 when c5missile come change some timeline to have a better dps
    if 0:
        conf['acl'] = acl12
        adv_test.test(module(), conf, verbose=0)

    conf['acl'] = acl21
    adv_test.test(module(), conf, verbose=0)


