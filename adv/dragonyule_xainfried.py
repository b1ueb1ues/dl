from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Dragonyule_Xainfried

class Dragonyule_Xainfried(Adv):
    a1 = ('dc', 1)
    a3 = ('primed_att', 0.08)

    conf = {}
    conf['slots.a'] = A_Dogs_Day()+Primal_Crisis()
    conf['slots.d'] = Ariel()
    conf['acl'] = """
        `dragon.act("s end")
        `s3, not self.s3_buff
        `s1
        `s2, x=5
        """
    coab = ['Blade','Bow','Tobias']

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.buff_class = Dummy if adv.slots.c.ele != 'wind' else Teambuff if adv.condition('buff all team') else Selfbuff

    def s1_proc(self, e):
        self.buff_class(e.name,0.2,15,'crit','chance').on()

    def s2_proc(self, e):
        self.dragonform.charge_gauge(50)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)

