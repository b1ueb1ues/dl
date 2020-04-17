from core.advbase import *

def module():
    return Nicolas

class Nicolas(Adv):
    conf = {}
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s1
        `s2
        `s3
        """
    coab = ['Blade','Ku_Hai','Lin_You']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)

