import adv_test
import adv
from wep.sword import flame as weapon
from core.timeline import *
from core.log import *


def module():
    return Naveed

class Naveed(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 4*1.70   ,
        "s1_sp"       : 2590   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.9    ,

        "s2_dmg"      : 0   ,
        "s2_sp"       : 4800   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.1    ,

        "mod_d"   : ('att'  , 'passive' , 0.6) ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        #"mod_wp2" : ('crit' , 'passive' , 0.06) ,
        #"mod_wp3" : ('fs'   , 'passive' , 0.20) ,
        #"mod_wp4" : ('s'    , 'passive' , 0.10) ,
        } )
    conf.update(weapon.conf)

    def init(this):
        this.s1level = 0
        pass

    def s1_proc(this, e):
        this.dmg_make("s1_missile",3*this.s1level*0.28)


    def s2_proc(this, e):
        this.s1level += 1
        if this.s1level > 5:
            this.s1level = 5
        adv.Buff("crown_double_buff",0.08,15).on()
    


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s2, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

