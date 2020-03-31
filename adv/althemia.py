import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Althemia

class Althemia(Adv):
    a1 = ('s',0.45,'hp100')
    conf = {}
    conf['slot.a'] = Candy_Couriers()+The_Fires_of_Hate()
    conf['slot.d'] = Fatalis()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
    """
    conf['afflict_res.poison'] = 0

    def s1_proc(self, e):
        self.afflics.poison('s1',100,0.482)

    def s2_proc(self, e):
        with KillerModifier('s2_killer', 'hit', 0.5, ['poison']):
            self.dmg_make("s2", 14.96)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

