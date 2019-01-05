import adv_test
from adv import *
from core.timeline import *
from core.log import *

from wep.blade import flame as weapon

def module():
    return Mikoto

class Mikoto(Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 0        ,
        "s1_sp"   : 4500     ,

        "s2_dmg"  : 0         ,
        "s2_sp"   : 4500      ,

        "mod_a"   : ('crit' , 'chance'  , 0.10) ,
        "mod_a2"  : ('crit' , 'chance'  , 0.08) ,
        } )
    conf.update(weapon.conf)

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


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5 and cancel
        """

    #conf['acl'] = """
    #    `s1
    #    `s3
    #    `s2
    #    """
    adv_test.test(module(), conf, verbose=0, mass=0)

