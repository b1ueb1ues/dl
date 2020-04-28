from core.advbase import *
from slot.d import *

def module():
    return Pia

class Pia(Adv):
    conf = {}
    conf['slots.d'] = AC011_Garland()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1
        `s2, fsc
        `fs, x=5
        """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']

    def s2_proc(self, e):
        self.energy.add(1, team=True)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)