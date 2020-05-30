from core.advbase import *
from slot.a import *

def module():
    return Summer_Luca

class Summer_Luca(Adv):
    a1 = ('a',0.1,'hp70')

    conf = {}
    conf['slots.a'] = RR()+Breakfast_at_Valerios()
    conf['slots.paralysis.a'] = Kung_Fu_Masters()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon, cancel
        `s1
        `s2
        `s3,seq=4
        `fs, x=5
        """
    coab = ['Blade','Dagger','Peony']

    def s2_proc(self, e):
        Spdbuff(e.name,0.2,10).on()
        self.energy.add(1.4) # means


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
