import adv_test
from adv import *
import adv.maribelle
import wep.wand


def module():
    return Maribelle_s3

class Maribelle_s3(adv.maribelle.Maribelle):
    def init(this):
        adv.maribelle.Maribelle.init(this)
        this.conf.update( {
            "s3_dmg"  : 4*2.71 ,
            "s3_sp"   : 8597   ,
            "s3_time" : 1.9    ,
            } )
        this.s3 = Skill("s3", this.conf["s3_sp"])


if __name__ == '__main__':
    conf = {}
    conf['al'] = {
        #'sp': ["s1","s2"],
        'x5': ["s1","s2","s3"],
        'x4': [],
        'x3': ["s1","s2","s3"],
        'x2': ["s1","s2","s3"],
        'x1': ["s1","s2","s3"],
        's':  ["s1","s2","s3"],
        } 

    adv_test.test(module(), conf, verbose=0)

