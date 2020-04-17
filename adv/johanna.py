from core.advbase import *
from slot.a import *

def module():
    return Johanna

class Johanna(Adv):
    conf = {}
    conf['slot.a'] = Kung_Fu_Masters()+Crystalian_Envoy()
    conf['acl'] = """
        `dragon.act("c3 s c2 end")
        `s1 
        `s2 
        `s3
        `fs,seq=5
        """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)