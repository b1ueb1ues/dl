import adv.adv_test
from adv import *
import adv
from slot.a import *

def module():
    return Alex

class Alex(adv.Adv):
    comment = 'not consider bk boost of her s2'
    a1 = ('s',0.35,'hp100')
    a3 = ('sp',0.05)

    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    conf['afflict_res.poison'] = 0
    conf['slot.a'] = TB()+TP()

    def s1_proc(this, e):
        this.afflics.poison('s1',100,0.396)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)


