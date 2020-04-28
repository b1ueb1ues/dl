from core.advbase import *
from slot.a import *

def module():
    return Francesca

class Francesca(Adv):
    a1 = ('fs',0.30)
    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+Primal_Crisis()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, x=4
        """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)