from core.advbase import *
from slot.a import *

def module():
    return Valentines_Addis

class Valentines_Addis(Adv):
    comment = 'use s2 once'

    a1 = ('k_poison',0.3)
    a3 = ('crisisattspd', 3)
    
    conf = {}
    conf['slots.a'] = The_Plaguebringer()+Primal_Crisis()
    conf['slots.poison.a'] = conf['slots.a']
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s2, self.hp > 30
        `s1
        `s4
    """
    coab = ['Wand','Curran','Summer_Patia']
    conf['afflict_res.poison'] = 0
    share = ['Veronica']

    def s1_proc(self, e):
        with CrisisModifier(e.name, 1.25, self.hp):
            self.afflics.poison(e.name, 120, 0.582)
            self.dmg_make(e.name, 8.60)

    def s2_proc(self, e):
        if self.hp > 30:
            self.set_hp(20)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
