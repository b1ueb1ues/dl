import adv_test
import adv
import wep.blade
from core.timeline import *
from core.log import *



def module():
    return Mikoto

class Mikoto(adv.Adv):
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
        this.atspd = 1.0
        this.stance = 0
        #this.s1 = Mikoto_s1_wait("s1", this.conf["s1_sp"])
        this.s1event = Event("s1buff", this.s1_end)
        this.s2event = Event("s2buff", this.s2_end)

    
    def sp_mod(this, name):
        return 1

    def att_mod(this):
        # calculate 20%crit to 12.42604% attack
        return 1.1242604

    def dmg_mod_x(this, name):
        if this.stance == 0:
            return 1
        elif this.stance == 1:
            return 1.15
        elif this.stance == 2:
            return 1.20

    def dmg_mod_s(this, name):
        return 1.25

    def speed(this):
        return this.atspd


    def s1_end(this, e):
        this.stance = 0
        log("buff",'s1','stance_end')
        Event("no_stance").trigger()


    def s1_proc(this, e):
        if this.stance == 0:
            this.dmg_make('s1',5.32*2)
            this.stance = 1
            this.s1event.on(now()+15)
            log("buff","s1","stance_1")
        elif this.stance == 1:
            this.dmg_make('s1',3.54*3)
            this.stance = 2
            this.s1event.on(now()+15)
            log("buff","s1","stance_2")
            Event("ruin_stance").trigger()
        elif this.stance == 2:
            this.dmg_make('s1',2.13*4+4.25)
            this.stance = 0
            Event("no_stance").trigger()
            log("buff","s1","stance_end")

    def s2_end(this, e):
        this.atspd = 1.0
        log("buff","s2","end     ")

    def s2_proc(this, e):
        this.atspd = 1.2
        log("buff","s2","start   ")
        this.s2event.on(now()+10)

    def s3_proc(this, e):
        pass


if __name__ == '__main__':
    conf = {}

    conf['acl'] = """
        /s1, seq==5 and cancel
        /s2, seq==0 
        """
    adv_test.test(module(), conf, verbose=0)

