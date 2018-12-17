import adv
import wep.wand


class Lily(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 9.68   ,
        "s1_sp"   : 2490     ,
        "s1_time" : 246/60.0 ,

        "s2_dmg"  : 9.74   ,
        "s2_sp"   : 5909     ,
        "s2_time" : 106/60.0 ,

        "s3_dmg"  : 0        ,
        "s3_sp"   : 0        ,
        "s3_time" : 0        ,
        } )
    conf.update(wep.wand.conf)

    def sp_mod(this, name):
        return 1

    def dmg_mod(this, name):
        return 1

    def str_mod(this, name):
        return 1.15
    
    def init(this):
        this.s1.charge(20000)
        this.s2.charge(20000)
        this.s3.charge(20000)

    def s1_proc(this, e):
        pass
    def s2_proc(this, e):
        pass
    def s3_proc(this, e):
        pass
