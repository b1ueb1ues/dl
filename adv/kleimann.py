import adv_test
import adv
import wep.wand


def module():
    return Kleimann

class Kleimann(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 9.84  ,
        "s1_sp"   : 2854     ,
        "s1_time" : 1.9, #114/60.0 ,

        "s2_dmg"  : 4.19*2   ,
        "s2_sp"   : 7090     ,
        "s2_time" : 1.8, #109/60.0 ,

        "s3_dmg"  : 0        ,
        "s3_sp"   : 0        ,
        "s3_time" : 0        ,
        } )
    conf.update(wep.wand.conf)

    def sp_mod(this, name):
        return 1

    def dmg_mod_s(this, name):
        return 1.45*1.11

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
    conf['al'] = {
        #'sp': ["s1","s2"],
        'x5': ["s1","s2"],
        'x4': [],
        'x3': [],
        'x2': [],
        'x1': [],
        's':  ["s1","s2"],
        } 

    adv_test.test(module(), conf, verbose=0)

