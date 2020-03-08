import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Xainfried

class Xainfried(Adv):
    a1 = ('dc', 4)
    a3 = ('dt', 0.25)
    conf = {}
    conf['slot.a'] = RR()+JotS()
    conf['slot.d'] = Siren()
    conf['acl'] = """
        `s1
        `s2
        `fs, x=5
        """
    conf['afflict_res.frostbite'] = 0

    def s1_proc(self, e):
        with Modifier('s1killer', 'frostbite_killer', 'hit', 0.3):
            self.dmg_make("s1", 2.30)
            self.hits += 1
            self.afflics.frostbite('s1',120,0.41)
            self.dmg_make("s1", 6.90)
            self.hits += 3

    def s2_proc(self, e):
        self.dragonform.charge_gauge(10)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

