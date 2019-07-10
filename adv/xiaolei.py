import adv_test
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
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel 
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=-2)
