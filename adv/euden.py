import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Euden

class Euden(Adv):
    a1 = ('dc', 4)
    conf = {}
    conf['slot.d'] = Apollo()
    conf['slot.a'] = The_Shining_Overlord()+Elegant_Escort()
    conf['acl'] = """
        `dragon, cancel
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `fs, x=3
        """

    conf['cond_afflict_res'] = 0
    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100

    def s1_proc(this, e):
        this.afflics.burn('s1',110,0.883)
        this.dragonform.charge_gauge(3)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)