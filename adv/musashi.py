import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
from slot.a import *

def module():
    return Musashi

class Musashi(Adv):
    a1 = ('lo',0.40)
    a3 = ('od',0.08)
    conf = {}
    conf['slot.d'] = Vayu()
    conf['slot.a'] = RR()+The_Fires_of_Hate()
    conf['acl'] = """
        `s2, seq=5
        `s1
        `s3, s
        """
    conf['afflict_res.poison'] = 0

    def s1_proc(this, e):
        this.afflics.poison('s1',110,0.53)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

