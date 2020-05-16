from core.advbase import *
from slot.a import *

def module():
    return Zardin

class Zardin(Adv):
    a1 = ('a',0.10,'hp100')
    
    conf = {}
    conf['slots.a'] = Primal_Crisis()+The_Shining_Overlord()
    conf['acl'] = """
        `dragon.act('c3 s end'), not self.afflics.frostbite.get()
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    coab = ['Xander', 'Dagger', 'Yurius']

    def d_coabs(self):
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Xander','Dagger','Wand']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)