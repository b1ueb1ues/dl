from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Halloween_Odetta

class Halloween_Odetta(Adv):

    conf = {}
    conf['slot.a'] = Mega_Friends() + Primal_Crisis()
    conf['slot.d'] = Dragonyule_Jeanne()
    conf['slots.frostbite.a'] = conf['slot.a']
    conf['acl'] = """
        `s2, cancel
        `s1, fsc
        `s3, fsc
        `fs, x=2
        """
    coab = ['Axe2', 'Xander', 'Dagger']
    a1 = ('primed_defense', 0.10)
    a3 = ('bt',0.2)

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    def s2_proc(self, e):
        self.buff_class('s2',0.2,15).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
