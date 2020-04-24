from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Marth

class Marth(Adv):
    comment = 'last boost once at start (team DPS not considered)'

    a1 = ('prep',100)
    a3 = ('cc',0.13,'hit10')
    
    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+Elegant_Escort()
    conf['acl'] = """
        `dragon, s=2
        `s3, not self.s3_buff
        `s2
        `s1, fsc
        `fs, x=3
    """
    coab = ['Blade', 'Wand', 'Joe']

    def d_coabs(self):
        if self.duration <= 60:
            self.coab = ['Blade','Wand','Gala_Sarisse']

    def init(self):
        self.stance = 0

    def s1_proc(self, e):
        self.afflics.burn('s1',120,0.97)

    def s2_proc(self, e):
        with KillerModifier('s2_killer', 'hit', 1.0, ['burn']):
            self.dmg_make("s2", 8.99)
        if self.stance == 0:
            self.stance = 1
            Selfbuff('s21',0.1,10).on()
        elif self.stance == 1:
            self.stance = 2
            Teambuff('s22',0.1,10).on()
        elif self.stance == 2:
            self.stance = 0
            Teambuff('s23',0.1,10).on()
            Spdbuff('s23s',0.3,10, wide='team').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)