if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

from adv import *
import adv.maribelle


def module():
    return Maribelle_s3

class Maribelle_s3(adv.maribelle.Maribelle):
    name = 'maribelle'
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
            "s3.dmg"      : 4*2.71 ,
            "s3.sp"       : 8597   ,
            "s3.startup"  : 0.1    ,
            "s3.recovery" : 1.9    ,
        })

    adv_test.test(module(), conf, verbose=0)

