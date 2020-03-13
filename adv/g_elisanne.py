import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Gala_Elisanne

class Gala_Elisanne(Adv):
    a3 = ('primed_att',0.10)

    conf = {}
    conf['slots.a'] = BB()+FWHC()
    conf['slots.d'] = Halloween_Maritimus()
    conf['acl'] = """
        `s1
        `fs, seq=5
        """

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    def prerun(self):
        self.s2.autocharge_init(1536).on()

    def s1_proc(self, e):
        self.buff_class('s2',0.3,15).on()

    def s2_proc(self):
        self.energy.add(3)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

