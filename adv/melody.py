import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.blade import wind as weapon

def module():
    return Melody

class Melody(adv.Adv):
    conf = {}
    conf.update( {
        "s1_buff"     : [0.15, 15, 'att'] ,
        "s1_sp"       : 2987   ,

        "s2_dmg"      : 2.64*3 ,
        "s2_sp"       : 4784   ,

        "mod_p"   : ('crit'  , 'chance', 0.08) ,
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

