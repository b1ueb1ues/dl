import adv_test
import adv
from wep.wand import shadow as weapon


def module():
    return Althemia

class Althemia(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 8.95   ,
        "s1_sp"       : 2759   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.45   , #114/60.0 ,

        "s2_dmg"      : 8.05   ,
        "s2_sp"       : 5570   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.4    , #114/60.0 ,

        "mod_a"   :("s",'passive',0.3),
        "mod_d"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        #"mod_sp" : ('sp' , 'ex' , 0.15) ,
        } )
    conf.update(weapon.conf)


if __name__ == '__main__':
    conf = {}

    # s2 after s1 will increase kleimann's damage a little since his s2's sp is too strange

    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel 
        `s2, s=1
        """

    # add little fs to increace damage
    if 1:
        conf['acl'] = """
            `fs, seq=5 and s1.charged >= 2500
            `s1, seq=5 and cancel or pin='fs'
            `s2, seq=5 and cancel or pin='fs'
            """
    if 0:  # add some sphaste also work!
        conf.update( {
            "mod_sp":('sp','ex',0.11)
            } )
        conf['acl'] = """
            `s1, seq=5 and cancel
            `s2, seq=5 and cancel 
            """

    adv_test.test(module(), conf, verbose=0)

