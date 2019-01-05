import adv_test
import adv

from wep.bow import light as weapon

def module():
    return Luca

class Luca(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg" : 7.71 ,
        "s1_sp"  : 2504 ,

        "s2_dmg" : 7.77 ,
        "s2_sp"  : 5115 ,

        "mod_a" : ('att' , 'passive' , 0.13)  ,
        } )
    conf.update(weapon.conf)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        """

    adv_test.test(module(), conf, verbose=0)

