import adv_test
from adv import *
from core.timeline import *
from core.log import *

from wep.lance import light as weapon

def module():
    return H_Elisanne

class H_Elisanne(Adv):
    conf = {}
    conf.update( {
        "s1_dmg" : 115*7 /100.0 ,
        "s1_sp"  : 2450         ,

        "s2_dmg" : 83*10 /100.0 ,
        "s2_sp"  : 5252         ,

        "mod_a"  : ('s', 'passive', 0.3) ,
        } )
    conf.update(weapon.conf)

    def init(this):
        this.stance = 0
        this.s1buff1 = Buff("s1_buff1",0.1, 10, 'att')
        this.s1buff2 = Buff("s1_buff2",0.1, 15, 'att')


    def s1_proc(this, e):
        if this.stance == 0:
            this.stance = 1
        elif this.stance == 1:
            this.s1buff1.on()
            this.stance = 2
        elif this.stance == 2:
            this.s1buff2.on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

