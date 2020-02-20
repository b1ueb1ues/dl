import adv.adv_test
from core.advbase import *
from core.advbase import *

def module():
    return Xiao_Lei

class Xiao_Lei(Adv):
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
    adv.adv_test.test(module(), conf)
