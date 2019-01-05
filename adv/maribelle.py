import adv_test
import adv

from wep.wand import wind as weapon

def module():
    return Maribelle

class Maribelle(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg" : 1.61*6 ,
        "s1_sp"  : 2648   ,

        "s2_dmg" : 2.44*4 ,
        "s2_sp"  : 5838   ,

        "mod_a"  : ('s'   , 'passive' , 0.4) ,
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

