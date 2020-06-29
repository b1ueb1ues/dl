from core.advbase import *
from slot.a import *

def module():
    return Linus

class Linus(Adv):
    # comment = 'do not use weapon skill'
    conf = {}
    conf['slots.a'] = Summer_Paladyns()+Primal_Crisis()
    conf['slots.paralysis.a'] = RR()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon
        `s1 
        `s2
        `s3, x=4
        `s4
        `fs, x=5
        """
    coab = ['Blade','Dagger','Peony']
    share = ['Ranzal']

    def d_slots(self):
        if self.duration <= 120:
            self.conf['slots.a'] = Resounding_Rendition() + Breakfast_at_Valerios()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)