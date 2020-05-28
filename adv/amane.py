from core.advbase import *

def module():
    return Amane

class Amane(Adv):
    a3 = ('bk',0.2)
    a1 = ('prep',0.75)
    
    conf = {}
    conf['acl'] = """
        `dragon
        `s2
        `s1
        `s3, x=5
        """
    coab = ['Blade','Halloween_Elisanne','Peony']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)