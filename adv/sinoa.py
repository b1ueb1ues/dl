import adv_test
import adv
from core.timeline import *
from core.log import *
import random

from wep.wand import flame as weapon

def module():
    return Sinoa

class Sinoa(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 0      ,
        "s1_sp"   : 3817   ,

        "s2_dmg"  : 2*4.43 ,
        "s2_sp"   : 5422   ,

        } )
    conf.update(weapon.conf)
    def init(this):
        random.seed()

    def s1_proc(this, e):
        r = random.random()
        if r<0.25  :
            adv.Buff('s1_att',0.15,15,'att').on()
        elif r<0.5 :
            adv.Buff('s1_crit',0.15,15,'crit').on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = '''
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        '''
    adv_test.test(module(), conf, verbose=0, mass=1)


