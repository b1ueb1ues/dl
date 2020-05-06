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
        `s1
        `s3,fsc
        `fs,seq=5
    """
    coab = ['Tiki', 'Xander', 'Dagger']
    conf['afflict_res.bog'] = 100

    def s1_proc(self, e):
        self.dmg_make('s1',2.27)
        self.afflics.bog.on('s1', 90)
        self.dmg_make('s1',4.54)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)