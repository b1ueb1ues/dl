import adv.adv_test
from core.advbase import *
from slot.a import *
import slot.a
import slot.w

def module():
    return Beautician_Zardin

class Beautician_Zardin(Adv):
    a3 = ('s',0.35,'hp70')

    conf = {}
    comment = 'no s2'
    conf['slots.a'] = RR()+JotS()
    conf['acl'] = """
        `s1
        `s3, seq=5
        """
    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = RR()+BN()

    def s1_proc(self, e):
        self.energy.add(1)

    def s2_proc(self, e):
        self.energy.add(2)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


