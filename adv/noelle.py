import adv.adv_test
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
    conf['slots.d'] = Ariel()
    conf['slots.a'] = Candy_Couriers()+A_Dogs_Day()

    conf['acl'] = """
        `s1
        `s2, x=5
        `s3, x=5
        """

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    def s1_proc(self, e):
        self.buff_class('s1',0.25,15).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

