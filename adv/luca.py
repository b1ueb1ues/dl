import adv_test
import adv
from wep.bow import light as weapon


def module():
    return Luca

class Luca(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 7.71 ,
        "s1_sp"       : 2504 ,
        "s1_startup"  : 0.1  ,
        "s1_recovery" : 2.15 ,

        "s2_dmg"      : 7.77 ,
        "s2_sp"       : 5115 ,
        "s2_startup"  : 0.1  ,
        "s2_recovery" : 1.9  ,

        "mod_a" : ('att'    , 'passive' , 0.13)  ,
        "mod_d"      : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"     : ('s'    , 'passive' , 0.25) ,
        "mod_wp2"    : ('crit' , 'chance'  , 0.06) ,
        #"mod_ex"     : ('s'    , 'ex'      , 0.15) ,
        #"mod_ex2"    : ('att'  , 'ex'      , 0.10) ,
        } )
    conf.update(weapon.conf)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        """

    adv_test.test(module(), conf, verbose=0)

