import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Cassandra

class Cassandra(Adv):
    comment = 'no counter damage; s2 drops combo'
    a1 = ('prep_charge',0.05)
    a3 = ('ro', 0.15)

    conf = {}
    conf['slots.a'] = Candy_Couriers()+The_Plaguebringer()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3
    """
    conf['afflict_res.poison'] = 0

    def prerun(self):
        self.hp = 80

        if self.condition('reflect 500 damage on every s2'):
            self.s2reflect = 500
        else:
            self.s2reflect = 0

    def s1_proc(self, e):
        self.afflics.poison('s1',120,0.582)

    def s2_proc(self, e):
        self.dmg_make('o_s2_reflect', self.s2reflect * 11, fixed=True)
        with CrisisModifier('s2', 1, self.hp):
            self.dmg_make('s2',9.72)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

