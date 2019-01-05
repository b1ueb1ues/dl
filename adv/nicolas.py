import adv_test
import adv

from wep.wand import wind as weapon


def module():
    return Nicolas

class Nicolas(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 8.95   ,
        "s1_sp"       : 2785   ,

        "s2_dmg"      : 8.05   ,
        "s2_sp"       : 5518   ,

        } )
    conf.update(weapon.conf)




if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        """

    adv_test.test(module(), conf, verbose=0)

