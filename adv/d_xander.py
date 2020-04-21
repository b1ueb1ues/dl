from core.advbase import *
from slot.d import *

def module():
    return Dragonyule_Xander

class Dragonyule_Xander(Adv):
    a3 = ('sp',0.05)

    conf = {}
    conf['slot.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel or s
        `s3, seq=5 and cancel
    """
    coab = ['Summer_Celliera', 'Blade', 'Thaniel']

    def prerun(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    def s2_proc(self, e):
        self.energy.add(1, team=self.condition('buff all team'))
        self.buff_class('s2', 0.15, 10)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)