import adv_test
import adv
from core.timeline import *
from core.log import *

from wep.wand import light as weapon

def module():
    return Amane

class Amane(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 4.92*2  ,
        "s1_sp"       : 2711    ,

        "s2_buff"     : [0.15, 10, 'att'] ,
        "s2_sp"       : 11449     ,

        } )
    conf.update(weapon.conf)

    def init(this):
        this.charge("prep","75%")



if __name__ == '__main__':
    conf = {}
    acl12 = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    acl21 = """
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5
        """ 
    # test that 21 is better than 12
    # s3 when c5missile come change some timeline to have a better dps
    if 0:
        conf['acl'] = acl12
        adv_test.test(module(), conf, verbose=0)

    conf['acl'] = acl21
    adv_test.test(module(), conf, verbose=0)


