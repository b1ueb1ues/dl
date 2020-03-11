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
    
    def s1_proc(self, e):
        self.afflics.burn('s1',120,0.97)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
