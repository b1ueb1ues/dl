import adv_test
import adv
import wep.blade
from core.timeline import *
from core.log import *



def module():
    return Melody

class Melody(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 0   ,
        "s1_sp"       : 2987   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.1    ,

        "s2_dmg"      : 2.64*3   ,
        "s2_sp"       : 4784   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.1    ,

        #"s3_dmg"      : 3.54*3 ,
        #"s3_sp"       : 8030   ,
        #"s3_startup"  : 0.1    ,
        #"s3_recovery" : 2.7    ,

        "mod_p"   : ('crit'  , 'chance', 0.08) ,
        "mod_d"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        } )
    conf.update(wep.blade.conf)

    def init(this):
        pass

    def s1_proc(this, e):
        adv.Buff("s1",0.15,15,'att').on()

    



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

