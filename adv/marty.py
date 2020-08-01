from core.advbase import *

def module():
    return Marty

class Marty(Adv):
    a1 = ('sp',0.05)

    conf = {}
    conf['acl'] = """
        `dragon, s
        `s3, fsc and not self.s3_buff
        `s4, fsc
        `s1, fsc
        `fs, x=2
        """
    coab = ['Blade', 'Marth', 'Dagger2']
    share = ['Ranzal']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)