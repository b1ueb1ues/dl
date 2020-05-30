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
        `s1,fsc
        `s2,fsc
        `s3,fsc
        `fs, seq=2 and cancel
    """
    coab = ['Blade', 'Yurius', 'Dagger']

    def s1_proc(self, e):
        self.dmg_make(f'o_{e.name}_boost',self.conf[f'{e.name}.dmg']*0.05*len(self.all_buffs))


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
