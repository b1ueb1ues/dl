import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Valentines_Melody

class Valentines_Melody(Adv):
    a3 = ('k_poison',0.3)

    conf = {}
    conf['slots.a'] = KFM()+Jewels_of_the_Sun()
    conf['slot.d'] = Freyja()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1
        `s2
        `fs, x=5
    """
    conf['cond_afflict_res'] = 0

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.poison.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.poison.resist=100
        if this.condition('s1 defdown for 10s'):
            this.s1defdown = 1
        else:
            this.s1defdown = 0

    def init(this):
        del this.slots.c.ex['axe']
        this.slots.c.ex['vmelody'] = ('ex', 'axe2')

    def s1_proc(this, e):
        if this.s1defdown :
            Debuff('s1',0.15,10,1).on()
    
    def s2_proc(this, e):
        this.afflics.poison('s2', 120, 0.582)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0, mass=0)
