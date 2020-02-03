import adv.adv_test
import adv
from slot.d import *

def module():
    return Philia

class Philia(adv.Adv):
    a1 = ('a',0.1,'hp100')
    conf = {}
    conf['slot.d'] = Garland()
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        """
    conf['cond_afflict_res'] = 0

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.paralysis.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.paralysis.resist=100

    def s2_proc(this, e):
        this.afflics.paralysis('s2',90,0.60)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

