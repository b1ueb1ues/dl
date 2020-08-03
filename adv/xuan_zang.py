from core.advbase import *
from slot.a import *

def module():
    return Xuan_Zang

class Xuan_Zang(Adv):
    a3 = ('cc',0.06,'hp70')
    
    conf = {}
    conf['slots.a'] = The_Wyrmclan_Duo()+Primal_Crisis()
    conf['slots.burn.a'] = Resounding_Rendition()+Me_and_My_Bestie()
    conf['acl'] = """
        `dragon, s=2
        `s3, not self.s3_buff
        `s2
        `s1
        `s4
        `fs, x=5
        """
    coab = ['Blade', 'Marth', 'Dagger2']
    share = ['Ranzal']

    def s1_proc(self, e):
        with KillerModifier(e.name, 'hit', 0.2, ['debuff']):
            self.dmg_make(e.name, 7.53)

    def s2_proc(self, e):
        Debuff(e.name,0.1,20,0.7).on()
        Debuff(f'{e.name}_atk',0.05,20,0.7,'attack').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
