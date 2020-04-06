from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Yaten

class Yaten(Adv):
    a1 = ('epassive_att_crit', 3)
    a3 = ('energized_att', 0.20)
    conf = {}
    conf['slot.a'] = The_Shining_Overlord()+JotS()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2, fsc and self.energy() < 4
        `fs, x=3
    """

    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = TSO()+BN()

    def s1_proc(self, e):
        if self.energy() == 5:
            self.dmg_make('o_s1_boost',6*0.69)
        self.energy.add(1)

    def s2_proc(self, e):
        self.energy.add(2, team=True)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)