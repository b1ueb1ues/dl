import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Summer_Luca

class Summer_Luca(Adv):
    a1 = ('a',0.1,'hp70')

    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3,seq=4
        `fs, x=5
        """
    conf['slots.a'] = KFM()+FitF()
    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = KFM()+HoH()

    def s2_proc(self, e):
        Spdbuff('s2',0.2,10).on()
        self.energy.add(1.4) # means


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
