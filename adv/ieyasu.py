import adv_test
from adv import *
from core.timeline import *
from core.log import *
from module.bleed import Bleed
import random

from wep.blade import shadow as weapon


def module():
    return Ieyasu

class Ieyasu(Adv):
    conf = {}
    conf.update( {
        "s1_dmg" : 8*1.19   ,
        "s1_sp"  : 2467     ,

        "s2_dmg" : 0        ,
        "s2_sp"  : 7913     ,

        "mod_a"  : ('crit' , 'damage'  , 0.2) ,
        "mod_a2" : ('crit' , 'chance'  , 0.1) ,
        } )
    conf.update(weapon.conf)

    def s2ifbleed(this):
        if this.s2buff.get()!=0:
            if this.bleed._static.stacks > 0:
                return 0.15
        return 0


    def init(this):
        this.s2buff = Buff("s2",0.15, 15, 'crit')
        this.s2buff.modifier.get = this.s2ifbleed
        this.bleed = Bleed("g_bleed",0).reset()
        random.seed()

    def s1_proc(this, e):
        if random.random() < 0.8:
            Bleed("s1_bleed", 1.46).on()


    def s2_proc(this, e):
        this.s2buff.on()

    def s3_proc(this, e):
        pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0, mass=1)

