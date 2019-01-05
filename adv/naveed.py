import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.sword import flame as weapon

def module():
    return Naveed

class Naveed(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 4*1.70 ,
        "s1_sp"   : 2590   ,

        "s2_dmg"  : 0      ,
        "s2_sp"   : 4800   ,

        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
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

