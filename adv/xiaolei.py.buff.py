if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

import adv
from adv import *

def module():
    return Xiaolei

class Xiaolei(adv.Adv):
    a1 = ('s',0.2)

    def s2_proc(this, e):
        Teambuff('s2cc',0.08,10,'crit','rate').on()
        Teambuff('s2cd',0.40,10,'crit','dmg').on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, fsc
        `s1, fsc
        `s3, fsc
        `fs, seq=5
        """ 
    adv_test.test(module(), conf, verbose=-2)


