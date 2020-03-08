import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Renelle

class Renelle(Adv):
    a1 = ('cc',0.15,'hit15')
    conf = {}
    conf['afflict_res.burn'] = 0
    conf['slot.d'] = Dreadking_Rathalos()
    conf['slot.a'] = TB()+EE()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, x=2
        """

    def s1_proc(self, e):
        self.afflics.burn('s1',100,0.803)
    
    def s2_proc(self, e):
        self.afflics.burn('s2',100,0.803)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

