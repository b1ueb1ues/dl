import adv_test
from adv import *
import adv.maribelle


def module():
    return Maribelle_s3

class Maribelle_s3(adv.maribelle.Maribelle):
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        `s3, s
        """
        
    conf.update({
            "s3_dmg"      : 4*2.71 ,
            "s3_sp"       : 8597   ,
            "s3_startup"  : 0.1    ,
            "s3_recovery" : 1.9    ,
        })

    adv_test.test(module(), conf, verbose=0)

