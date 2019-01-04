import adv_test
import adv
from wep.sword import flame as weapon
from core.timeline import *
from core.log import *



def module():
    return Euden

class Euden(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 3.75*2   ,
        "s1_sp"       : 2376   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.85   ,

        "s2_dmg"      : 6.38   ,
        "s2_sp"       : 4880   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 2.7    ,

        "mod_d"   : ('att'  , 'passive' , 0.6) ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,

        } )

    conf.update(weapon.conf)

    def init(this):
        pass
    
    def s2_proc(this, e):
        adv.Buff('armorbreak',1/0.955-1, 10, 'att','debuff').on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s2, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

