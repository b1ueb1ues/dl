import adv_test
import adv
import wep.wand


def module():
    return Maribelle

class Maribelle(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 1.61*6 ,
        "s1_sp"   : 2648   ,
        "s1_time" : 2.7    ,

        "s2_dmg"  : 2.44*4 ,
        "s2_sp"   : 5838   ,
        "s2_time" : 1.8    ,

        "s3_dmg"  : 0      ,
        "s3_sp"   : 0      ,
        "s3_time" : 0      ,
        } )
    conf.update(wep.wand.conf)

    def sp_mod(this, name):
        return 1

    def dmg_mod_s(this, name):
        return (1.4+0.25)*1.15

    def att_mod(this):
        return 1.6

    def init(this):
        this.charge("prep", "100%")
        this.s1buff = adv.Buff('armorbreak',(1.0/0.95-1)/2+1,10)


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

