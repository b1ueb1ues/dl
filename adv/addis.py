import adv_test
from adv import *
from core.timeline import *
from core.log import *
from module.bleed import Bleed
import random

from wep.blade import wind as weapon


def module():
    return Addis

class Addis(Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 4*2.16  ,
        "s1_sp"       : 2537    ,

        "s2_dmg"      : 0       ,
        "s2_sp"       : 4877    ,

        } )
    conf.update(weapon.conf)

    def getbleedpunisher(this):
        if this.bleed._static.stacks > 0:
            return 0.08
        return 0

    def init(this):
        this.s2buff = Buff("s2",0.25, 10, 'att')
        this.bleedpunisher = Modifier("bleed","att","punisher",0.08)
        this.bleedpunisher.get = this.getbleedpunisher
        this.bleed = Bleed("g_bleed",0).reset()
        random.seed()

    def s1_proc(this, e):
        if this.s2buff.get():
            if random.random() < 0.8:
                Bleed("s1_bleed", 1.46).on()


    def s2_proc(this, e):
        this.s2buff.on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or s=2
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0, mass=1)

