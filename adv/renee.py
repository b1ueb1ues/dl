from core.advbase import *
from slot.d import *

def module():
    return Renee

class Renee(Adv):
    a1 = ('primed_crit_chance', 0.6,5)

    conf = {}
    conf['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1
        `s2
        `s3, seq=5
        `fs, seq=5
        """
    coab = ['Blade', 'Xander', 'Tiki']
    conf['afflict_res.bog'] = 100

    def s1_proc(self, e):
        self.dmg_make(e.name,1.11)
        self.afflics.bog.on(e.name, 100)
        self.dmg_make(e.name,5.55)

    def s2_proc(self, e):
        Event('defchain')()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)