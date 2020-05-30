
from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Noelle

class Noelle(Adv):
    comment = 'use Freyja & Castle Cheer Corps in 4DPS team'
    a1 = ('bt',0.25)
    a3 = ('primed_defense',0.08)

    conf = {}
    conf['slots.a'] = A_Dogs_Day()+Primal_Crisis()
    conf['slots.d'] = Ariel()
    conf['acl'] = """
        `s4
        `s1
        `s3
        """
    coab = ['Tiki','Tobias','Bow']
    share = ['Patia','Summer_Luca']

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.buff_class = Dummy if adv.slots.c.ele != 'wind' else Teambuff if adv.condition('buff all team') else Selfbuff

    def s1_proc(self, e):
        self.buff_class(e.name,0.25,15).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)

