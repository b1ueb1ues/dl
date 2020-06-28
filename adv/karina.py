from core.advbase import *
from slot.a import *

def module():
    return Karina

class Karina(Adv):
    a3 = ('prep','50%')

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Breakfast_at_Valerios()
    conf['slots.frostbite.a'] = Primal_Crisis()+His_Clever_Brother()
    conf['acl'] = """
        `dragon.act('c3 s end'), x=5
        `s3
        `s1
        `s2
        `s4
    """
    coab = ['Dagger', 'Xander', 'Wand']
    share = ['Gala_Elisanne', 'Ranzal']

    def s1_proc(self, e):
        self.dmg_make(f'o_{e.name}_boost',self.conf[f'{e.name}.dmg']*0.05*self.buffcount)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)