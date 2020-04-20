from core.advbase import *
from slot.a import *

def module():
    return Julietta

class Julietta(Adv):
    comment = 'no fs & no s2'

    def s2_proc(self, e):
       adv.Event('defchain')()

    conf = {}
    conf['slots.a'] = RR()+Breakfast_at_Valerios()
    conf['acl'] = """
        `dragon
        `s1
        `s3,seq=5
        """
    coab = ['Blade','Dagger','Halloween_Elisanne']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)