import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.sword import flame as weapon


def module():
    return Euden

class Euden(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 3.75*2 ,
        "s1_sp"   : 2376   ,

        "s2_dmg"  : 6.38   ,
        "s2_sp"   : 4880   ,

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

