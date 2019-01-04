import adv_test
import adv
from wep.blade import wind as weapon
from core.timeline import *
from core.log import *



def module():
    return Melody

class Melody(adv.Adv):
    conf = {}
    conf.update( {
        "s1_buff"     : [0.15, 15, 'att'] ,
        "s1_sp"       : 2987   ,
        "s1_startup"  : 0.25   ,
        "s1_recovery" : 0.9    ,

        "s2_dmg"      : 2.64*3 ,
        "s2_sp"       : 4784   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 2.75   ,

        "mod_p"   : ('crit'  , 'chance', 0.08) ,
        "mod_d"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
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

