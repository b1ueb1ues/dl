from core.advbase import *
from slot.a import *

def module():
    return Xander

class Xander(Adv):
    comment = 'c2+fs'

    a3 = ('fs',0.50)

    conf = {}
    conf['slots.a'] = TSO()+Primal_Crisis()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, x=2
    """
    coab = ['Blade', 'Yurius', 'Dagger']

    def s1_proc(self, e):
        self.dmg_make(f'o_{e.name}_boost',self.conf[f'{e.name}.dmg']*0.05*self.buffcount)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
