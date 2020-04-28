from core.advbase import *
from slot.d import *

def module():
    return Aeleen

class Aeleen(Adv):
    conf = {}
    conf['slots.d'] = AC011_Garland()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1
        `fs, seq=5
        """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']
    a1 = ('bt',0.25)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)