import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Halloween_Elisanne

class Halloween_Elisanne(Adv):
    a1 = ('s',0.3)
    conf = {}
    conf['slots.a'] = RR()+JotS()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3
        `fs, seq=5
        """

    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = HoH()+JotS()

    def prerun(self):
        self.stance = 0

    def s1latency(self, e):
        Teambuff("s1_buff",0.1,15).on()

    def s1_proc(self, e):
        if self.stance == 0:
            self.stance = 1
        elif self.stance == 1:
            Timer(self.s1latency).on(2.5)
            self.stance = 2
        elif self.stance == 2:
            Timer(self.s1latency).on(2.5)
            self.stance = 0

    def s2_proc(self, e):
        self.charge('s2',500)



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
