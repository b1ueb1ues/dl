import adv_test
import adv
import wep.wand


def module():
    return Lily

class Lily(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 9.68   ,
        "s1_sp"       : 2490   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 4      ,

        "s2_dmg"      : 9.74   ,
        "s2_sp"       : 5909   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.85   ,

        "s3_dmg"      : 4*2.71 ,
        "s3_sp"       : 8597   ,
        "s3_startup"  : 0.1    ,
        "s3_recovery" : 1.9    ,
        } )
    conf.update(wep.wand.conf)

    def sp_mod(this, name):
        return 1

    def dmg_mod_s(this, name):
        return 1.25*1.15

    def att_mod(this):
        return (1.4+0.15) * 115.4/101.4 #calc crit as att
    
    def init(this):
        this.charge("prep", "100%")

    def s1_proc(this, e):
        pass
    def s2_proc(this, e):
        pass
    def s3_proc(this, e):
        pass

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        #prep=0
        #if pin=='prep': prep=1
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5 and cancel
        `s3, s=1
        `s1, pin='prep'
        """

    adv_test.test(module(), conf, verbose=0)



