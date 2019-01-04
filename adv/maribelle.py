import adv_test
import adv
from wep.wand import wind as weapon


def module():
    return Maribelle

class Maribelle(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 1.61*6 ,
        "s1_sp"       : 2648   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 2.7    ,

        "s2_dmg"      : 2.44*4 ,
        "s2_sp"       : 5838   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.8    ,

        "mod_a_fullhp" : ('s'    , 'passive' , 0.4)  ,
        "mod_d"      : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"     : ('s'    , 'passive' , 0.25) ,
        "mod_wp2"    : ('crit' , 'chance'  , 0.06) ,
        #"mod_ex"     : ('s'    , 'ex'      , 0.15) ,
        #"mod_ex2"    : ('att'  , 'ex'      , 0.10) ,
        } )
    conf.update(weapon.conf)


    def init(this):
        this.charge("prep", "100%")
        this.s1buff = adv.Buff('armorbreak',(1.0/0.95-1)/2,10)


    def s1_proc(this, e):
        this.s1buff.on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        """

    adv_test.test(module(), conf, verbose=0)

