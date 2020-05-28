from core.advbase import *
from slot.a import *

def module():
    return Karina

class Karina(Adv):
    a3 = ('prep','50%')

    conf = {}
    conf['slots.a'] = RR()+Breakfast_at_Valerios()
    conf['slots.frostbite.a'] = Primal_Crisis()+His_Clever_Brother()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1
        `s2, seq=4
        `s3, fsc
        `fs, seq=5
    """
    coab = ['Dagger', 'Xander', 'Wand']

    def s1_proc(self, e):
        self.dmg_make(f'o_{e.name}_boost',self.conf[f'{e.name}.dmg']*0.05*len(self.all_buffs))

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)