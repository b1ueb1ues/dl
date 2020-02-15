import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Valentines_Melody

class Valentines_Melody(Adv):
    comment = 'c4fsf c5 c4 s1'
    a3 = ('k_poison',0.3)

    conf = {}
    conf['slots.a'] = KFM()+The_Fires_of_Hate()
    conf['slot.d'] = Vayu()
    conf['acl'] = """
        `s1
        `s2
        `s3, this.afflics.poison.get() and this.mod('def')!=1
        `fsf, x=4 and (s1.charged == this.sp_val(4))
    """
    conf['afflict_res.poison'] = 0

    def prerun(this):
        this.s1defdown = this.condition('s1 defdown for 10s')

    def init(this):
        del this.slots.c.ex['axe']
        this.slots.c.ex['axe2'] = ('ex', 'axe2')

    def s1_proc(this, e):
        if this.s1defdown:
            Debuff('s1',0.15,10,1).on()
    
    def s2_proc(this, e):
        this.afflics.poison('s2', 120, 0.582)
        if this.afflics.poison.get():
            # has 5s cd irl
            Teambuff('a1',0.10*this.afflics.poison.get(),10).on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
