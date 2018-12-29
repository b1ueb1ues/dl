import adv_test
import adv
import wep.blade
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

        "s2_dmg"      : 0       ,
        "s2_sp"       : 4877   ,
        "s2_startup"  : 0.1+0.5 , #65/60
        "s2_recovery" : 1.1-0.5 , #65/60

        #"s3_dmg"      : 4*2.71  ,
        #"s3_sp"       : 8597    ,
        #"s2_startup"  : 0.1     ,
        #"s3_recovery" : 1.9     , #117/60
        "mod_a"   : ('att'  , 'passive' , 0.08)  ,
        "mod_d"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        } )
    conf.update(wep.blade.conf)


    def init(this):
        pass


    def s2_proc(this, e):
        adv.Buff("s2",0.25,10,'att').on()


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


