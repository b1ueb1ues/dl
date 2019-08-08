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
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel 
        `s3, seq=5 and cancel
        """

    def s2_proc(this, e):
        Teambuff('s2cc',0.08,10,'crit','rate').on()
        Teambuff('s2cd',0.40,10,'crit','dmg').on()



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)
