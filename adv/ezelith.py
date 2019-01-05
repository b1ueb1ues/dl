import adv_test
from adv import *
from core.timeline import *
from core.log import *
import random

from wep.dagger import flame as weapon

def module():
    return Ezelith

class Ezelith(Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 10*0.57+2.50 ,
        "s1_sp"   : 2400  ,

        "s2_dmg"  : 0     ,
        "s2_sp"   : 8940  ,

        "mod_a"   : ('att', 'broken_p', 0.3*0.15) ,
        } )
    conf.update(weapon.conf)

    def init(this):
        random.seed()
        this.s2buff = Buff("s2",0.15, 15,'att')

    def s2_proc(this, e):
        this.s2buff.on()

    def dmg_proc(this, name, amount):
        if name[0] != 'x':
            return
        if this.s2buff.get():
            r = random.random()
            if r < 0.5:
                Buff("s2_ab",-0.05,5,'def').on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """

    #conf['acl'] = """
    #    `s1
    #    `s3
    #    `s2
    #    """
    adv_test.test(module(), conf, verbose=0, mass=1)

