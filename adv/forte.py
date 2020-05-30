from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Forte

class Forte(Adv):
    comment = 'Cleo coab hits 10 stack buff limit'
    a3 = ('k_poison', 0.30)

    conf = {}
    conf['slots.a'] = The_Red_Impulse()+Heralds_of_Hinomoto()
    conf['slots.d'] = Epimetheus()
    conf['slots.poison.d'] = Shinobi()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s3, not self.s3_buff
        `s2
        `s1
        `fs, x=5
        """
    coab = ['Ieyasu','Wand','Bow']

    def prerun(self):
        self.dgauge_charge = 4

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.dgauge_charge = 0

    def s1_proc(self, e):
        self.dragonform.charge_gauge(self.dgauge_charge, dhaste=False)
        with KillerModifier('s1_killer', 'hit', 0.3, ['poison']):
            self.dmg_make(e.name, 11.34)

    def s2_proc(self, e):
        self.dragonform.charge_gauge(self.dgauge_charge, dhaste=False)
        Selfbuff(e.name, 0.20, 15, 'att', 'buff')

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)