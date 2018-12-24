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
        "s1_dmg"  : 0      ,
        "s1_sp"   : 4500   ,
        "s1_time" : 1.9    ,

        "s2_dmg"  : 0      ,
        "s2_sp"   : 4500   ,
        "s2_time" : 1.1    ,

        "s3_dmg"  : 3.54*3 ,
        "s3_sp"   : 8030   ,
        "s3_time" : 2.7      ,
        } )
    conf.update(wep.blade.conf)

    def init(this):
        this.s1buff = Buff("s1",1, 15)
        this.s2buff = Buff("s2",1.2, 10)

    
    def sp_mod(this, name):
        return 1

    def att_mod(this):
        # calculate 20%crit to 12.42604% attack
        return 1.1242604*1.6

    def dmg_mod_x(this, name):
        return this.s1buff.get()

    def dmg_mod_s(this, name):
        return 1.25

    def speed(this):
        return this.s2buff.get()

    def s1_proc(this, e):
        buff = this.s1buff.get()
        if buff == 1:
            stance = 0
        elif buff == 1.15:
            stance = 1
        elif buff == 1.2:
            stance = 2

        if stance == 0:
            this.dmg_make('s1',5.32*2)
            this.s1buff.set(1.15).on()
        elif stance == 1:
            this.dmg_make('s1',3.54*3)
            this.s1buff.off()
            this.s1buff.set(1.2).on()
        elif stance == 2:
            this.dmg_make('s1',2.13*4+4.25)
            this.s1buff.off().set(1)

    def s2_proc(this, e):
        this.s2buff.on()

    def s3_proc(this, e):
        pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 
        `s1, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

