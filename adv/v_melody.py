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
    conf['slot.d'] = Ariel()
    conf['acl'] = """
        `s1
        `s2
        `s3, cancel and self.mod('def')!=1
        `fsf, x=4 and (s1.charged == self.sp_val(4))
    """
    conf['afflict_res.poison'] = 0

    def prerun(self):
        self.s1defdown = self.condition('s1 defdown for 10s')

    def init(self):
        del self.slots.c.ex['axe']
        self.slots.c.ex['axe2'] = ('ex', 'axe2')

    def s1_proc(self, e):
        if self.s1defdown:
            Debuff('s1',0.15,10,1).on()
    
    def s2_proc(self, e):
        self.afflics.poison('s2', 120, 0.582)
        if self.afflics.poison.get():
            # has 5s cd irl
            Teambuff('a1',0.10*self.afflics.poison.get(),10).on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
