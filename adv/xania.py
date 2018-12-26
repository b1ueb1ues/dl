import adv_test
import adv
import wep.wand
from core.timeline import *
from core.log import *



def module():
    return Xania

class Xania(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 8.85   ,
        "s1_sp"   : 2759   ,
        "s1_time" : 1.9    ,

        "s2_dmg"  : 8.05   ,
        "s2_sp"   : 5570   ,
        "s2_time" : 1.9    ,

        } )
    conf.update(wep.wand.conf)

    def init(this):
        pass
    
    def sp_mod(this, name):
        return 1

    def att_mod(this):
        return 1.6

    def dmg_mod_x(this, name):
        return 1

    def dmg_mod_s(this, name):
        return (1.25+1.2-1) * 1.08






if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

