from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Althemia

class Althemia(Adv):
    a1 = ('s',0.45,'hp100')
    
    conf = {}
    conf['slots.a'] = Candy_Couriers()+The_Fires_of_Hate()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s2
        `s4
        `s1,self.s3_buff
        `dragon.act('c3 s end'),x=5
    """
    coab = ['Blade','Delphi','Gala_Alex']
    conf['afflict_res.poison'] = 0
    share = ['Curran']

    def d_coabs(self):
        if self.duration <= 60:
            self.coab = ['Blade','Bow',"Gala_Alex"]

    def s1_proc(self, e):
        self.afflics.poison(e.name,100,0.482)

    def s2_proc(self, e):
        with KillerModifier('s2_killer', 'hit', 0.5, ['poison']):
            self.dmg_make(e.name, 14.96)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
