from core.advbase import *

def module():
    return Rawn

class Rawn(Adv):
    conf = {}
    conf['acl'] = """
        `dragon, fsc
        `s1
        `s2
        `s3
        `fs, x=4
        """
    coab = ['Blade','Wand','Halloween_Elisanne']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)