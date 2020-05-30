from core.advbase import *
from slot.a import *

def module():
    return Xuan_Zang

class Xuan_Zang(Adv):
    a3 = ('cc',0.06,'hp70')
    
    conf = {}
    conf['slots.a'] = The_Wyrmclan_Duo()+Primal_Crisis()
    conf['slots.burn.a'] = Resounding_Rendition()+Elegant_Escort()
    conf['acl'] = """
        `dragon, s=2
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, x=5
        """
    coab = ['Blade', 'Marth', 'Tiki']

    def s1_proc(self, e):
        if self.mod('def')!= 1:
            self.dmg_make(f'o_{e.name}_boost',2.51*3*0.2*0.91)

    def s2_proc(self, e):
        Debuff(e.name,0.1,20,0.7).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
