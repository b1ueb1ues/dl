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
    conf['slots.d'] = PopStar_Siren()
    conf['acl'] = """
        `dragon
        `s1
        `s3, seq=5
        """
    coab = ['Tobias','Peony','Bow']

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    def s1_proc(self, e):
        self.buff_class('s2',0.25,15).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)