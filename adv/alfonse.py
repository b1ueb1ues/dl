from core.advbase import *
from slot.a import *

def module():
    return Alfonse

class Alfonse(Adv):
    a1 = [('lo',0.40, 10.0),('lo',0.10,-1)]
    a3 = ('sp',0.10)

    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon, fsc
        `s1
        `s2,fsc
        `s3,fsc
        `fs, x=3
    """
    coab = ['Sharena','Dagger','Peony']

    def prerun(self):
        self.hp = 80

    def s1_before(self, e):
        Selfbuff('s1buff',0.20,12).on()

    def s1_proc(self, e):
        self.afflics.paralysis('s1',120, 0.97)

    def s2_proc(self, e):
        with CrisisModifier('s2', 1.00, self.hp):
            self.dmg_make('s2', 7.32)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)