import adv.adv_test
from core.advbase import *
from slot.a import *
#from slot.d import *

def module():
    return Nobunaga

class Nobunaga(Adv):
    a1 = ('a',0.2,'hit15')
    conf = {}
    conf['slot.a'] = RR()+Primal_Crisis()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, x=5
        """

    def prerun(self):
        self.ba = 0
    
    def s1_proc(self, e):
        self.ba = 1

    def s2_proc(self, e):
        if self.ba == 1:
            self.ba = 0
            self.dmg_make('o_s1_boost',11.18)

    def fs_proc(self, e):
        if self.ba == 1:
            self.ba = 0
            self.dmg_make('o_s1_boost',11.18)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
