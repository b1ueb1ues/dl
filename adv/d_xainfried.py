import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Dragonyule_Xainfried

class Dragonyule_Xainfried(Adv):
    a1 = ('dc', 1)
    a3 = ('primed_att', 0.08)

    conf = {}
    conf['slots.d'] = Ariel()
    conf['slots.a'] = ADD()+Primal_Crisis()
    conf['acl'] = """
        `s1
        `s2, x=5
        `s3, x=5
        """

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    def s1_proc(self, e):
        self.buff_class('s1',0.2,15,'crit','chance').on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

