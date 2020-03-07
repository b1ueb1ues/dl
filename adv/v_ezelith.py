import adv.adv_test
from core.advbase import *
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Valentines_Ezelith

class Valentines_Ezelith(Adv):
    a3 = ('bk',0.2)
    conf = {}
    conf['slot.a'] = EE()+DD()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, fsc and not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, seq=2
    """
    conf['afflict_res.burn'] = 0

    def prerun(self):
        self.ehit = 0
        self.has_ehit = self.condition('always connect hits')

    def dmg_proc(self, name, amount):
        if self.has_ehit and self.hits // 35 > self.ehit:
            self.energy.add(1)
            self.ehit = self.hits // 35

    def s1_proc(self, e):
        self.afflics.burn('s1',110,0.883)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

