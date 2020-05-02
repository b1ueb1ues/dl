from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Rex

class Rex(Adv):
    conf = {}
    conf['slots.a'] = Summer_Paladyns()+Primal_Crisis()
    conf['slots.frostbite.a'] = KFM()+His_Clever_Brother()
    conf['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1 
        `s2,seq=4
        `s3,seq=4
        `fs,seq=5
        """
    coab = ['Blade', 'Xander', 'Dagger']

    def d_slots(self):
        if self.duration <= 120:
            self.conf['slots.a'] = Resounding_Rendition() + Breakfast_at_Valerios()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)