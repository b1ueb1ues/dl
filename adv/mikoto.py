import adv_test
from adv import *
import wep.blade
from core.timeline import *
from core.log import *



def module():
    return Mikoto

class Mikoto(Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 0        ,
        "s1_sp"       : 4500     ,
        "s1_startup"  : 0.1      ,
        "s1_recovery" : 1.9      ,

        "s2_dmg"      : 0        ,
        "s2_sp"       : 4500     ,
        "s2_startup"  : 0.25     ,
        "s2_recovery" : 1.1-0.15 ,

        "s3_dmg"      : 3.54*3   ,
        "s3_sp"       : 8030     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 2.7      ,

        "mod_a"   : ('crit' , 'chance'  , 0.10) ,
        "mod_a2"   : ('crit' , 'chance'  , 0.08) ,
        "mod_d"   : ('att'  , 'passive' , 0.60) ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'chance'  , 0.06) ,
        #"mod_ex"  : ('att'  , 'ex'      , 0.10) ,
        #"mod_ex2"  : ('s'  , 'ex'      , 0.15) ,
        } )
    conf.update(wep.blade.conf)

    def init(this):

        this.s1buff = Buff("s1",0, 15, 'x')
        this.s2buff = Buff("s2",0.2, 10)

    def speed(this):
        return 1+this.s2buff.get()

    def s1_proc(this, e):
        buff = this.s1buff.get()
        if buff == 0:
            stance = 0
        elif buff == 0.15:
            stance = 1
        elif buff == 0.2:
            stance = 2
        if stance == 0:
            this.dmg_make('s1',5.32*2)
            this.s1buff.set(0.15).on()
        elif stance == 1:
            this.dmg_make('s1',3.54*3)
            this.s1buff.off()
            this.s1buff.set(0.2).on()
        elif stance == 2:
            this.dmg_make('s1',2.13*4+4.25)
            this.s1buff.off().set(0)

    def s2_proc(this, e):
        this.s2buff.on()

    def s3_proc(this, e):
        pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

