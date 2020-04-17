import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Odetta

class Odetta(Adv):
    comment = 'c2+fs'

    conf = {}
    conf['slots.a'] = RR() + The_Lurker_in_the_Woods()
    conf['acl'] = """
        `s2, fsc
        `s1, fsc
        `s3, fsc
        `fs, seq=2
        """

    a1 = ('a',0.1,'hp70')
    a3 = ('bt',0.2)

    def init(self):
        if self.condition('buff all team'):
            self.s2_proc = self.c_s2_proc

    def c_s2_proc(self, e):
        Teambuff('s2',0.15,15).on()

    def s2_proc(self, e):
        Selfbuff('s2',0.15,15).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
