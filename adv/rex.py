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
        `s3
        `s1
        `s4, x=4 
        `s2, x=4
        `fs, x=5
    """
    coab = ['Blade', 'Xander', 'Renee']
    share = ['Gala_Elisanne', 'Ranzal']

    def d_slots(self):
        if self.duration <= 120:
            self.conf['slots.a'] = Resounding_Rendition()+Breakfast_at_Valerios()
        if self.duration <= 120 and self.duration > 60:
            self.conf['slots.frostbite.a'] = Primal_Crisis()+His_Clever_Brother()

    def d_coabs(self):
        if self.sim_afflict and (self.duration > 120 or self.duration <= 60):
            self.coab = ['Blade', 'Xander','Yurius']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)