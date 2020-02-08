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
        `s3, not this.s3_buff_on
        `s1
        `s2
        `fs, (s1.charged>=s1.sp-this.sp_val('fs')) or (s2.charged>=s2.sp-this.sp_val('fs'))
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
    adv.adv_test.test(module(), conf, verbose=-2)
