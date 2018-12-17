import adv
import wep.blade


class Mikoto(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 10    ,
        "s1_sp"   : 4800     ,
        "s1_time" : 167/60.0 ,

        "s2_dmg"  : 0        ,
        "s2_sp"   : 0        ,
        "s2_time" : 0        ,

        "s3_dmg"  : 0        ,
        "s3_sp"   : 0        ,
        "s3_time" : 0        ,
        } )
    conf.update(wep.blade.conf)

    def sp_mod(this, name):
        return 1


    def dmg_mod(this, name):
        return 1

    def init(this):
        pass


    def s1_proc(this, e):
        pass
    def s2_proc(this, e):
        pass
    def s3_proc(this, e):
        pass
