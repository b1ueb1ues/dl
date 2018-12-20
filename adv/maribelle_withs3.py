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
        s1,seq==4 and pin == 'x_cancel'
        s2,seq==4 and pin == 'x_cancel'
        """
        
    #conf.update({
            #"s3_dmg"  : 4*2.71 ,
            #"s3_sp"   : 8597   ,
            #"s3_time" : 1.9    ,
        #})

    adv_test.test(module(), conf, verbose=0)

