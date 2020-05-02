from core.advbase import *
from slot.a import *

def module():
    return Dragonyule_Malora

class Dragonyule_Malora(Adv):
    comment = 'c4fsf c5 c4 s1'
    a1 = ('od',0.13)

    conf = {}
    conf['slots.a'] = Summer_Paladyns() + Primal_Crisis()
    conf['slots.paralysis.a'] = Resounding_Rendition() + Spirit_of_the_Season()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s1
        `s2, self.def_mod()!=1
        `fsf, x=4 and (s1.charged == self.sp_val(4))
        """
    coab = ['Blade','Dagger','Peony']

    def prerun(self):
        if self.condition('buff all team'):
            self.s1debuff = Debuff('s1',0.15,15)
        else:
            self.s1debuff = None

    def s1_proc(self, e):
        if self.s1debuff is not None:
            self.s1debuff.on()
        self.dmg_make('s1',4.67,'s')
        self.hits += 1

    def s2_proc(self, e):
        if self.def_mod()!= 1:
            self.dmg_make('o_s2_boost',4.32*3*0.8)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)