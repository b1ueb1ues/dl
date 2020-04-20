from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Fjorm

class Fjorm(Adv):
    comment = 'last bravery once at start'
    a3 = [('prep',1.00), ('scharge_all', 0.05)]
    conf = {}
    conf['slots.a'] = Resounding_Rendition()+His_Clever_Brother()
    conf['slots.d'] = Siren()
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, x=5
        """
    coab = ['Blade', 'Wand', 'Xander']
    def prerun(self):
        Teambuff('last_bravery',0.3,15).on()

    def s1_proc(self, e):
        self.afflics.frostbite('s1',120,0.41)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)