import adv_test
import adv
from wep.wand import water as weapon


def module():
    return Lily

class Lily(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 9.68   ,
        "s1_sp"       : 2490   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 3.95   ,

        "s2_dmg"      : 9.74   ,
        "s2_sp"       : 5909   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.85   ,


        "mod_a_fullhp"   : ('att'  , 'passive' , 0.15)  ,
        "mod_d"   : ('att'  , 'passive' , 0.45)  ,
        "mod_d2"   : ('crit'  , 'passive' , 0.2)  ,
        #"mod_d3"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        "mod_ex" : ('s','ex',0.15)
        } )
    conf.update(weapon.conf)

    def init(this):
        this.charge("prep", "100%")


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



