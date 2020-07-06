from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Dragonyule_Xander

class Dragonyule_Xander(Adv):
    a3 = ('sp',0.05)

    conf = {}
    conf['slots.a'] = CC()+PC()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s3
        `s4
        `s1
        `s2, x=5 or s
    """
    coab = ['Tiki', 'Blade', 'Thaniel']
    share = ['Gala_Elisanne', 'Eugene']

    def prerun(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.buff_class = Teambuff if adv.condition('buff all team') else Selfbuff

    def s2_proc(self, e):
        self.energy.add(1, team=self.condition('buff all team'))
        self.buff_class(e.name, 0.15, 10)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)