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

        "mod_a_fullhp"   : ('att'  , 'passive' , 0.15)  ,
        #"mod_d"   : ('att'  , 'passive' , 0.45)  ,
        #"mod_d2"   : ('crit'  , 'passive' , 0.2)  ,
        "mod_d3"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        "mod_ex" : ('s','ex',0.15)
        } )
    conf.update(wep.wand.conf)

    
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
        `s3, s
        `s1, pin='prep'
        """

    adv_test.test(module(), conf, verbose=0)



