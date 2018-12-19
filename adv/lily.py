import adv_test
import adv
import wep.wand


def module():
    return Lily

class Lily(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 9.68     ,
        "s1_sp"   : 2490     ,
        "s1_time" : 4,

        "s2_dmg"  : 9.74     ,
        "s2_sp"   : 5909     ,
        "s2_time" : 1.85 ,

        "s3_dmg"  : 4*2.71   ,
        "s3_sp"   : 8597     ,
        "s3_time" : 1.9        ,
        } )
    conf.update(wep.wand.conf)

    def sp_mod(this, name):
        return 1

    def dmg_mod_s(this, name):
        return 1.25*1.15

    def att_mod(this):
        return 1.15
    
    def init(this):
        this.charge("prep", "100%")

    def s1_proc(this, e):
        pass
    def s2_proc(this, e):
        pass
    def s3_proc(this, e):
        pass

if __name__ == '__main__':
    conf = {}
    conf['al'] = {
        #'sp': ["s1","s2"],
        'x5': ["s1","s2","s3"],
        'x4': [],
        'x3': ["s1","s2","s3"],
        'x2': ["s1","s2","s3"],
        'x1': ["s1","s2","s3"],
        's': ["s1","s2","s3"],
        } 

    adv_test.test(module(), conf, verbose=0)


