import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Wedding_Elisanne


class Wedding_Elisanne(Adv):
    comment = '2in1'
    a1 = ('sp',0.08)
    a3 = ('bc',0.13)

    conf = {}
    conf['acl'] = """
        `s1,fsc and s2.charged<s2.sp-749
        `s2
        `s3,fsc and not self.s2_debuff.get()
        `fs,seq=2 and cancel and ((s1.charged>=909 and not self.s2_debuff.get()) or s3.charged>=s3.sp)
        `fs,seq=3 and cancel
    """
    conf['slot.a'] = TSO()+JotS()
    def d_slots(self):
        if 'bow' in self.ex:
            self.conf.slot.a = TSO()+FRH()

    def prerun(self):
        self.s2_debuff = Debuff('s2defdown',0.15,10,1)
        self.s2_defdown = self.condition('s2 defdown for 10s')

    def s2_proc(self, e):
        if self.s2_defdown:
            self.s2_debuff = Debuff('s2defdown',0.15,10,1).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
