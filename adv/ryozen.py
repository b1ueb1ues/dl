import adv.adv_test
from core.advbase import *

def module():
    return Ryozen

class Ryozen(Adv):
    a3 = ('od',0.08)
    conf = {}
    conf['acl'] = """
        `dragon, cancel
        `s2
        `s3
        `fs, x=5
        """
    coab = ['Blade','Dagger','Peony']
    
    def s1_proc(self, e):
        Teambuff(e.name, 0.25, 15, 'defense').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)