from core.advbase import *
from slot.d import *

def module():
    return Orion

class Orion(Adv):
    a1 = ('cc',0.10,'hit15')
    a3 = ('prep', 0.50)
    conf = {}
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, x=5
    """
    coab = ['Ieysau','Wand','Axe2']

    def d_coabs(self):
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Ieyasu','Wand','Cleo']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)