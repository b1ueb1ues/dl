from core.advbase import *
from slot.a import *

def module():
    return Xander

class Xander(Adv):
    comment = 'c2+fs'

    a3 = ('fs',0.50)

    conf = {}
    conf['slots.a'] = TSO()+Primal_Crisis()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s3, fsc
        `s1, fsc
        `s2, fsc
        `s4, fsc
        `fs, x=2
    """
    coab = ['Blade', 'Yurius', 'Dagger']
    share = ['Gala_Elisanne', 'Ranzal']

    def s1_proc(self, e):
        self.dmg_make(f'o_{e.name}_boost',self.conf[f'{e.name}.dmg']*0.05*self.buffcount)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
