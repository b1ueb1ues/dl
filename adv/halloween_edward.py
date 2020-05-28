from core.advbase import *

def module():
    return Halloween_Edward

class Halloween_Edward(Adv):
    a1 = ('a',0.1,'hp100')

    conf = {}
    conf['acl'] = """
        `dragon
        `s1
        `s2, x=5
        `s3
        """
    coab = ['Halloween_Elisanne','Dagger','Peony']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)