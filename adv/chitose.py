from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Chitose

class Chitose(Adv):
    a3 = ('a',-0.1)

    conf = {}
    conf['slots.a'] = A_Game_of_Cat_and_Boar()+Memory_of_a_Friend
    conf['slots.paralysis.a'] = conf['slots.a']
    conf['slots.d'] = Tie_Shan_Gongzhu()
    conf['acl'] = """
        `s4
        `s1
        `s3
        """
    coab = ['Tobias','Peony','Bow']
    share = ['Patia','Summer_Luca']

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.buff_class = Dummy if adv.slots.c.ele != 'light' else Teambuff if adv.condition('buff all team') else Selfbuff

    def s1_proc(self, e):
        self.buff_class(e.name,0.25,15).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)