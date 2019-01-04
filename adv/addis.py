import adv_test
from adv import *
import wep.blade5b1 as weapon
from core.timeline import *
from core.log import *
from module.bleed import Bleed
import random



def module():
    return Addis

class Addis(Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 4*2.16   ,
        "s1_sp"       : 2537     ,
        "s1_startup"  : 0.1      ,
        "s1_recovery" : 1.9      ,

        "s2_dmg"      : 0        ,
        "s2_sp"       : 4877     ,
        "s2_startup"  : 0.25     ,
        "s2_recovery" : 1.1-0.15 ,


        "mod_d"   : ('att'  , 'passive' , 0.60) ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'chance'  , 0.06) ,
        #"mod_ex"  : ('att'  , 'ex'      , 0.10) ,
        #"mod_ex2"  : ('s'  , 'ex'      , 0.15) ,
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
        this.bleed = Bleed("g_bleed",0)
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
        `s1, seq=5 and cancel 
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

