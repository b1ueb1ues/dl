import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.axe import water as weapon


def module():
    return Karina

class Karina(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg" : 2*5.43 ,
        "s1_sp"  : 3033   ,

        "s2_dmg" : 4*2.57 ,
        "s2_sp"  : 5280   ,


        "mod_d" :[('att'  , 'passive' , 0.45)  ,
                  ('crit' , 'chance'  , 0.20)] ,
        } )
    conf.update(weapon.conf)

    def init(this):
        this.charge("prep","50%")



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `s3
        """
    adv_test.test(module(), conf, verbose=0)

