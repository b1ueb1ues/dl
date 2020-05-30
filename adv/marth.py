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
        self.phase['s2'] = 0

    def s1_proc(self, e):
        self.afflics.burn(e.name,120,0.97)

    def s2_proc(self, e):
        with KillerModifier('s2_killer', 'hit', 1.0, ['burn']):
            self.dmg_make(e.name, 8.99)
        self.phase[e.name] += 1
        if self.phase[e.name] == 0:
            Selfbuff(e.name,0.1,10).on()
        elif self.phase[e.name] == 1:
            Teambuff(e.name,0.1,10).on()
        elif self.phase[e.name] == 2:
            Teambuff(e.name,0.1,10).on()
            Spdbuff(f'{e.name}_spd',0.3,10, wide='team').on()
        self.phase[e.name] %= 3

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)