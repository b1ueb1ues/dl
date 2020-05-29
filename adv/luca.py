from core.advbase import *
from slot.a import *

def module():
    return Luca

class Luca(Adv):
    a1 = ('a',0.13,'hp100')

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon
        `s1
        `s2, fsc
        `s3
        `fs, seq=4
        """
    coab = ['Blade','Halloween_Elisanne','Peony']
    conf['afflict_res.paralysis'] = 0

    def s1_proc(self, e):
        self.afflics.paralysis(e.name,110,0.883)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)