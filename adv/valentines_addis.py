from core.advbase import *
from slot.a import *

def module():
    return Valentines_Addis

class Valentines_Addis(Adv):
    comment = 'use s2 once'

    a1 = ('k_poison',0.3)
    
    conf = {}
    conf['slots.a'] = The_Plaguebringer()+Primal_Crisis()
    conf['slots.poison.a'] = conf['slots.a']
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s2, self.hp > 30
        `s1
    """
    coab = ['Wand','Curran','Berserker']
    conf['afflict_res.poison'] = 0

    def prerun(self):
        self.a3atk = Selfbuff('a3atk',0.20,-1,'att','passive')
        self.a3spd = Spdbuff('a3spd',0.10,-1)

    def s1_proc(self, e):
        with CrisisModifier(e.name, 1.25, self.hp):
            self.afflics.poison(e.name, 120, 0.582)
            self.dmg_make(e.name, 8.60)

    def s2_proc(self, e):
        if self.hp > 30:
            self.set_hp(20)
            self.a3atk.on()
            self.a3spd.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
