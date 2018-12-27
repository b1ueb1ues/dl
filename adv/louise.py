import adv_test
import adv
import wep.bow as weapon


def module():
    return Louise

class Louise(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 2.12*4 ,
        "s1_sp"       : 2896   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.9 ,

        "s2_dmg"      : 2.69*3 ,
        "s2_sp"       : 5838   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.8    ,

        "s3_dmg"      : 0      ,
        "s3_sp"       : 0      ,
        "s3_startup"  : 0.1    ,
        "s3_recovery" : 1.9    ,

        "mod_a_od" : ('att'    , 'punisher' , 0.13/2)  ,
        "mod_d"      : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"     : ('s'    , 'passive' , 0.25) ,
        "mod_wp2"    : ('crit' , 'chance'  , 0.06) ,
        #"mod_ex"     : ('s'    , 'ex'      , 0.15) ,
        #"mod_ex2"    : ('att'  , 'ex'      , 0.10) ,
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
        """

    adv_test.test(module(), conf, verbose=0)

