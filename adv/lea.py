import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Lea

class Lea(Adv):
    comment = 'c2+fs'
    a1 = ('fs', 0.50)
    a3 = ('sp', 0.12, 'fs')
        
    conf = {}
    conf['slot.a'] = TSO()+EE()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, seq=2
        """
    conf['afflict_res.burn'] = 0
    
    def prerun(self):
        if self.condition('reflect 500 damage on every s2'):
            self.s2reflect = 500
        else:
            self.s2reflect = 0

    def s1_proc(self, e):
        self.afflics.burn('s1',120,0.97)

    def s2_proc(self, e):
        self.dmg_make('o_s2_reflect', self.s2reflect * 11, fixed=True)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
