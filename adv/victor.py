import adv.adv_test
from core.advbase import *
from module.bleed import Bleed
from slot.a import *
from slot.d import *

def module():
    return Victor

class Victor(Adv):
    a1 = ('a',0.13,'hp70')
    conf = {}
    conf['slots.d'] = Vayu()
    conf['slots.a'] = slot.a.RR()+slot.a.Beautiful_Nothingness()
    conf['acl'] = """
        `s1, self.bleed._static['stacks'] < 3
        `s2, seq=5
        `s3, seq=5
        """

    def d_slots(self):
        if 'bow' in self.ex:
            self.conf.slot.a = HoH()+JotS()

    def prerun(self):
        random.seed()
        self.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(self, e):
        if random.random() < 0.8:
            Bleed("s1", 1.46).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

