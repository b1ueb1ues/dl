from core.advbase import *
from slot.a import *

def module():
    return Rawn

class Rawn(Adv):
    conf = {}
    conf['slots.paralysis.a'] = Resounding_Rendition()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon, fsc
        `s1
        `s2
        `s3
        `fs, x=4
        """
    coab = ['Blade','Halloween_Elisanne','Peony']

    def s1_proc(self, e):
        Debuff(e.name, 0.05, 10, 0.4, 'attack').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)