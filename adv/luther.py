from core.advbase import *
from slot.d import *

def module():
    return Luther

class Luther(Adv):
    a1 = ('cc',0.10,'hit15')

    conf = {}
    conf ['slots.d'] = Nimis()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1
        `s2, x=5
        `fs, x=5
    """
    coab = ['Blade', 'Xander', 'Tiki']

    def s2_proc(self, e):
        Debuff(e.name, 0.05, 10, 0.9, 'attack').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)