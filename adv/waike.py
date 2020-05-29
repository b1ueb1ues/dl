from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Waike

class Waike(Adv):
    a1 = ('edge_bog', 40, 'hp100')

    conf = {}
    conf['slots.a'] = Primal_Crisis()+Mega_Friends()
    conf['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
        """
    coab = ['Blade', 'Xander', 'Tiki']
    conf['afflict_res.bog'] = 100

    def s2_proc(self, e):
        self.afflics.bog.on(e.name, 80)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
