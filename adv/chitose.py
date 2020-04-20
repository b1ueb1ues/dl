from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Chitose

class Chitose(Adv):
    a3 = ('a',-0.1)

    conf = {}
    conf['slots.a'] = A_Game_of_Cat_and_Boar()+United_by_One_Vision()
    conf['slots.paralysis.a'] = conf['slots.a']
    conf['slots.d'] = PopStar_Siren
    conf['acl'] = """
        `dragon
        `s1
        `s3, seq=5
        """
    coab = ['Blade','Bow','Tobias']

    def init(self):
        if self.condition('buff all team'):
            self.s1_proc = self.c_s1_proc

    def c_s1_proc(self, e):
        Teambuff('s1',0.25,15).on()

    def s1_proc(self, e):
        Selfbuff('s1',0.25,15).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)