from core.advbase import *
from slot.d import *

def module():
    return Erik

class Erik(Adv):
    a1 = ('fs',0.30)
    conf = {}
    conf['slots.d'] = Fatalis()
    conf['slots.poison.d'] = Shinobi()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2, fsc
        `fs, x=5
    """
    coab = ['Blade','Wand','Dagger']

    def s1_proc(self, e):
        with KillerModifier('s1_killer', 'hit', 0.5, ['poison']):
            self.dmg_make(e.name, 15.84)

    def s2_proc(self, e):
        with KillerModifier('s2_killer', 'hit', 0.5, ['poison']):
            self.dmg_make(e.name, 17.16)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)