import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Fjorm

class Fjorm(Adv):
    # comment = 'do not calc damage counter'
    a3 = ('prep', 100)
    conf = {}
    #conf['slot.d'] = DJ()
    conf['acl'] = """
        `s1
        `s2
        `s3, seq=5
        `fs, seq=5
        """

    def prerun(self):
        Teambuff('last bravery',0.3,15).on()
        if self.condition('reflect 500 damage on every s2'):
            self.s2reflect = 500
        else:
            self.s2reflect = 0

    def s2_proc(self, e):
        self.dmg_make('o_s2_reflect', self.s2reflect * 11, fixed=True)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


