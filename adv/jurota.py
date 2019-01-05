import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.blade import water as weapon

def module():
    return Jurota

class Jurota(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 8.78   ,
        "s1_sp"       : 2630   ,

        "s2_buff"     : [0.25, 5, 'att'] ,
        "s2_sp"       : 4101   ,

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

