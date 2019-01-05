import adv_test
import adv

from wep.bow import wind as weapon

def module():
    return Louise

class Louise(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 2.12*4 ,
        "s1_sp"       : 2896   ,

        "s2_dmg"      : 2.69*3 ,
        "s2_sp"       : 5838   ,

        "mod_a_od" : ('att' , 'punisher' , 0.13*0.45) ,
        } )
    conf.update(weapon.conf)

    def init(this):
        pass


    def s1_proc(this, e):
        pass



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """

    adv_test.test(module(), conf, verbose=0)

