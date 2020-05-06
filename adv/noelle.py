
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
        `s3, not self.s3_buff
        `s1
        """
    coab = ['Tiki','Tobias','Bow']

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    def s1_proc(self, e):
        self.buff_class('s1',0.25,15).on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)

