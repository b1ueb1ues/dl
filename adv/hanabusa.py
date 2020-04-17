import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Hanabusa

class Hanabusa(Adv):
    conf = {}
    conf['slots.a'] = RR()+JotS()
    conf['acl'] = """
        `s1
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """

    def prerun(self):
        self.stance = 0

    def s1_proc(self, e):
        if self.stance == 0:
            self.s1.sp = 2567
            self.stance = 1
            Timer(self.stanceend).on(20)
        elif self.stance == 1:
            self.dmg_make('s1',1.94)
            self.stance = 2
            Timer(self.stanceend).on(20)
        elif self.stance == 2:
            self.dmg_make('s1',2.51)
            self.s1.sp = 2840
            self.stance = 0

    def s2_proc(self, e):
        if self.stance == 0:
            Teambuff('s2',0.15,15).on()
        elif self.stance == 1:
            Teambuff('s2',0.15,18).on()
        elif self.stance == 2:
            Teambuff('s2',0.15,21).on()

    def stanceend(self, e):
        self.s1.sp = 2840
        self.stance = 0

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

