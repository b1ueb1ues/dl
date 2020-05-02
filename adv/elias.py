from core.advbase import *
from slot.a import *

def module():
    return Elias

class Elias(Adv):
    a3 = ('lo',0.4)
    conf = {}
    conf['slots.paralysis.a'] = RR()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon
        `s1, fsc
        `s3, fsc
        `s2, fsc
        `fs, x=4
        """
    coab = ['Blade','Halloween_Elisanne','Peony']

    def s2_proc(self, e):
        self.energy.add(1, team=True)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)