import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Althemia

class Althemia(Adv):
    a1 = ('s',0.45,'hp100')
    conf = {}
    conf['slot.a'] = Candy_Couriers()+The_Fires_of_Hate()
    conf['acl'] = """
        `s1
        `s2
        `s3
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

