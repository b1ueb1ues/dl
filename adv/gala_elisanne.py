from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Gala_Elisanne

class Gala_Elisanne(Adv):
    a3 = ('primed_att',0.10)

    conf = {}
    conf['slots.a'] = BB()+FWHC()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `s4
        `s1
        `s3
        `fsf, x=4
    """
    coab = ['Bow','Tobias', 'Renee']
    share = ['Patia','Summer_Luca']
    
    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.buff_class = Dummy if adv.slots.c.ele != 'water' else Teambuff if adv.condition('buff all team') else Selfbuff

    def prerun(self):
        self.s2.autocharge_init(900).on()

    def s1_proc(self, e):
        self.buff_class(e.name,0.3,15).on()

    def s2_proc(self, e):
        self.energy.add(3)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)