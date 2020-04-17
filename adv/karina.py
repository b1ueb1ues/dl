import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Karina

class Karina(Adv):
    a3 = ('prep','50%')
    conf = Conf()
    conf.slot.a = RR()+Breakfast_at_Valerios()

    def s1_proc(self, e):
        self.dmg_make('o_s1_boost',self.conf['s1.dmg']*0.05*len(self.all_buffs))

    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1
        `s2, seq=4
        `s3, fsc
        `fs, seq=5
        """
    coab = ['Dagger', 'Xander', 'Wand']
if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
