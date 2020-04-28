from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Valentines_Melody

class Valentines_Melody(Adv):
    comment = 'c4fsf c5 c4 s1'
    a1 = ('affteam_poison', 0.10, 10, 5)
    a3 = ('k_poison',0.3)

    conf = {}
    conf['slots.a'] = Kung_Fu_Masters()+The_Fires_of_Hate()
    conf['slots.d'] = Ariel()
    conf['slots.poison.d'] = AC011_Garland()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
        `fsf, x=4 and (s1.charged == self.sp_val(4))
    """
    coab = ['Blade','Eleonora','Lin_You']
    conf['afflict_res.poison'] = 0

    def prerun(self):
        self.s1defdown = self.condition('s1 defdown for 10s')

    def init(self):
        self.slots.c.coabs['Axe2'] = [None, 'axe2']

    def s1_proc(self, e):
        if self.s1defdown:
            Debuff('s1',0.15,10,1).on()
    
    def s2_proc(self, e):
        self.afflics.poison('s2', 120, 0.582)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)