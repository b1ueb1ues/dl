import adv.adv_test
from core.advbase import *
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Luca

class Luca(Adv):
    a1 = ('a',0.13,'hp100')
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
        """
    conf['afflict_res.paralysis'] = 0

    def s1_proc(this, e):
        this.afflics.paralysis('s1',110,0.883)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)
