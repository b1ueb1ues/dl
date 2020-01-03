if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *
from slot.d import *

def module():
    return Euden

class Euden(adv.Adv):
    a1 = ('dc', 0.10)
    conf ={}
    conf['slot.a'] = TSO()+EE()
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    conf['cond_afflict_res'] = 0
    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100

    def s1_proc(this, e):
        this.afflics.burn('s1',110,0.883)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

