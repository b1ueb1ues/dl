import adv.adv_test
from core.advbase import *
from slot.d import *

def module():
    return Philia

class Philia(Adv):
    a1 = ('a',0.1,'hp100')
    conf = {}
    conf['slot.d'] = Garland()
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        """
    conf['afflict_res.paralysis'] = 0

    def s2_proc(this, e):
        this.afflics.paralysis('s2',90,0.60)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

