import adv_test
import adv
import wep.wand


def module():
    return Kleimann

class Kleimann(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 9.84   ,
        "s1_sp"       : 2854   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.9    , #114/60.0 ,

        "s2_dmg"      : 4.19*2 ,
        "s2_sp"       : 7090   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.8    , #114/60.0 ,

        "s3_dmg"      : 0      ,
        "s3_sp"       : 0      ,
        "s3_startup"  : 0.1    ,
        "s3_recovery" : 1.9    ,

        "mod_a"   :("fs",'passive',0.4),
        "mod_a2"   :("s",'passive',0.2),
        "mod_d"   : ('att'  , 'passive' , 0.45)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        } )
    conf.update(wep.wand.conf)

    def init(this):
        pass


    def s1_proc(this, e):
        pass
    def s2_proc(this, e):
        pass
    def s3_proc(this, e):
        pass


if __name__ == '__main__':
    conf = {}


    # s2 after s1 will increase kleimann's damage a little since his s2's sp is too strange
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel 
        `s2, s=1
        """

    # add little fs to increace very little damage
    if 1:
        conf['acl'] = """
            `s1, seq=5 and cancel or pin='fs'
            `fs, seq=5 and this.s2.charged < 7090 and this.s2.charged > 6400
            `s2, seq=5 and cancel or pin='fs'
            `s2, s=1
            `s2, sp and seq=-1
            """

    adv_test.test(module(), conf, verbose=0)
    import core.log

