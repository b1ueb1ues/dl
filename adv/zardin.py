import adv_test
import adv
import wep.sword
from core.timeline import *
from core.log import *



def module():
    return Zardin

class Zardin(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 6.82   ,
        "s1_sp"       : 2443   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.9    ,

        "s2_dmg"      : 5.52   ,
        "s2_sp"       : 5225   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.9    ,

       # "s3_dmg"      : 1.65*5 ,
       # "s3_sp"       : 6847   ,
       # "s3_startup"  : 0.1    ,
       # "s3_recovery" : 2.7    ,

        "mod_a"   : ('att'  , 'passive' , 0.1) ,
        "mod_d"   : ('att'  , 'passive' , 0.6) ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,

        } )

    conf.update(wep.sword.conf)

    def init(this):
        pass
    



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s2, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

