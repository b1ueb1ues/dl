from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Xuan_Zang

class Xuan_Zang(Adv):
    a3 = ('cc',0.06,'hp70')
    
    conf = {}
    conf['slots.burn.a'] = Primal_Crisis()+Elegant_Escort()
    conf['slots.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1, fsc
        `s2, cancel
        `fs, x=4
        """
    coab = ['Blade', 'Wand', 'Marth']

    def s1_proc(self, e):
        if self.mod('def')!= 1:
            self.dmg_make('o_s1_boost',2.51*3*0.2*0.91)

    def s2_proc(self, e):
        Debuff('s2_defdown',0.1,20,0.7).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)