import adv_test
from adv import *
import adv.maribelle
import wep.wand


def module():
    return Maribelle_s3

class Maribelle_s3(adv.maribelle.Maribelle):
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        s1, seq==5 and pin == 'x_cancel'
        s2, seq==5 and pin == 'x_cancel'
        s1, pin == 'prep'
        s2, pin == 'prep'
        """
        
    #conf.update({
            #"s3_dmg"  : 4*2.71 ,
            #"s3_sp"   : 8597   ,
            #"s3_time" : 1.9    ,
        #})

    import time
    a = time.time()
    adv_test.test(module(), conf, verbose=0)
    b = time.time()
    print b-a

