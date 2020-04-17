from core.advbase import *
from slot.a import *

def module():
    return Francesca

class Francesca(Adv):
    a1 = ('fs',0.30)
    conf = {}
    conf['slot.a'] = TB()+PC()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s1
        `s2
        `s3
        `fs, x=4
        """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)