import adv_test
import adv

from wep.wand import shadow as weapon

def module():
    return Kleimann

class Kleimann(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 9.84   ,
        "s1_sp"   : 2854   ,

        "s2_dmg"  : 4.19*2 ,
        "s2_sp"   : 7090   ,

        "mod_a"  : ("fs", 'passive', 0.4),
        "mod_a2" : ("s" , 'passive', 0.2),
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
    import core.log

