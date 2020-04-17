import adv.adv_test
from core.advbase import *
from slot.a import *
#from slot.d import *

def module():
    return Nobunaga

class Nobunaga(Adv):
    comment = 'use s2 instead of fs to dispel when possible'

    a1 = ('a',0.2,'hit15')
    conf = {}
    conf['slots.a'] = RR()+Primal_Crisis()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, x=5 and self.s2.charged<self.s2.sp-self.sp_val(5)
        """

    def prerun(self):
        self.ba = 0
    
    def s1_proc(self, e):
        self.ba = 1

    def s2_proc(self, e):
        if self.ba == 1:
            self.ba = 0
            self.dmg_make('o_s1_boost',11.18)
            self.dmg_make('o_s2_boost',self.conf.s2.dmg*0.3)

    def fs_proc(self, e):
        if self.ba == 1:
            self.ba = 0
            self.dmg_make('o_s1_boost',11.18)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
