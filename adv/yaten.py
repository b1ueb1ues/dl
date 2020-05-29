from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Yaten

class Yaten(Adv):
    a1 = ('epassive_att_crit', 3)
    a3 = ('energized_att', 0.20)
    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+United_by_One_Vision()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2, fsc and self.energy() < 4
        `fs, x=3
    """
    coab = ['Ieyasu','Wand','Dagger']

    def d_coabs(self):
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Ieyasu','Wand','Bow']

    def s1_proc(self, e):
        if self.energy() == 5:
            self.dmg_make(f'o_{e.name}_boost',6*0.69)
        self.energy.add(1)

    def s2_proc(self, e):
        self.energy.add(2, team=True)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
