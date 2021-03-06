from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Jakob

class Jakob(Adv):
    a1 = ('prep','50%')

    conf = {}
    conf['slots.frostbite.a'] = Primal_Crisis()+His_Clever_Brother()
    conf['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s3
        `s1
        `s4
        `fs, seq=5
    """
    coab = ['Dagger2', 'Xander', 'Dagger']
    share = ['Gala_Elisanne', 'Ranzal']
    conf['afflict_res.bog'] = 100

    def s1_proc(self, e):
        self.dmg_make(e.name,2.27)
        self.afflics.bog.on(e.name, 90)
        self.dmg_make(e.name,4.54)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)