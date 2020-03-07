import adv.adv_test
from core.advbase import *
from slot.d import *

def module():
    return Dragonyule_Cleo

class Dragonyule_Cleo(Adv):
    a1 = ('a',0.13,'hp70')
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5 and cancel or fsc
        `s3, fsc
        `fs, seq=5
        """

    def prerun(self):
        self.has_ehit = self.condition('always connect hits')
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff
        self.stance = 0
        self.ehit = 0

    def dmg_proc(self, name, amount):
        if self.has_ehit and self.hits // 30 > self.ehit:
            self.energy.add(1)
            self.ehit = self.hits // 30

    def s1_proc(self, e): # buggy lvl3 s1
        self.energy.add(1, team=self.condition('buff all team'))
        if self.stance == 0:
            self.stance = 1
        elif self.stance == 1:
            self.stance = 2
            self.buff_class('s1s',0.1,10).on()
        elif self.stance == 2:
            self.stance = 0
            self.buff_class('s1s',0.1,10).on()
            self.buff_class('s1c',0.08,10,'crit','chance').on()




if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)