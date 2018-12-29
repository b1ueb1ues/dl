import adv_test
import adv
import wep.blade
from core.timeline import *
from core.log import *



def module():
    return Jurota

class Jurota(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 8.78   ,
        "s1_sp"       : 2630   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.9    ,

        "s2_dmg"      : 0   ,
        "s2_sp"       : 4101   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.1    ,

        #"s3_dmg"      : 0 ,
        #"s3_sp"       : 0   ,
        #"s3_startup"  : 0.1    ,
        #"s3_recovery" : 2.7    ,

        "mod_d"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        } )
    conf.update(wep.blade.conf)

    def init(this):
        this.s2buff = adv.Buff("s2",0.25,5,'att')

    def s2_proc(this, e):
        this.s2buff.on()

    



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

