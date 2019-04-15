import adv_test
import adv
from adv import *

def module():
    return Xiaolei

class Xiaolei(adv.Adv):
    a1 = ('s',0.2)

#    def pre(this):
#        if this.condition('s2 in lv1'):
#            this.conf['s2.sp'] = 3909
#            this.s2_proc = this.c_s2_proc

    def s2_proc(this, e):
        Teambuff('s2cc',0.08,10,'crit','rate').on()
        Teambuff('s2cd',0.40,10,'crit','dmg').on()

    def c_s2_proc(this, e):
        Teambuff('s2cc',0.05,10,'crit','rate').on()
        Teambuff('s2cd',0.30,10,'crit','dmg').on()


if __name__ == '__main__':
    conf = {}
    acl12 = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel 
        `s3, seq=5 and cancel
        """
    acl21 = """
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5
        """ 
    if 1:
        conf['acl'] = acl12
        adv_test.test(module(), conf, verbose=0)
    else:
        conf['acl'] = acl21
        adv_test.test(module(), conf, verbose=0)


