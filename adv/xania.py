if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *
from slot.d import *

def module():
    return Xania

class Xania(adv.Adv):
    a1 = ('s',0.35)
    conf = {}
    conf['slot.d'] = Apollo()
    conf['acl'] = """
        `s1
        `s2
        `s3
        """
    conf['cond_afflict_res'] = 0
    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100

    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)

    def s2_proc(this, e):
        this.afflics.burn('s2',100,0.803)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)
