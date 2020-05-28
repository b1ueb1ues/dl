from core.advbase import *
from slot.a import *
from slot.d import Leviathan
import adv.fjorm

def module():
    return Fjorm

class Fjorm(adv.fjorm.Fjorm):
    comment = '4x Fjorm in 20.55s with sufficient dprep'
    a3 = [('prep',1.00), ('scharge_all', 0.05)]
    a2 = [('dp',50)] # team dprep
    conf = {}
    conf['slots.a'] = Unexpected_Requests()+Valiant_Crown()
    conf['slots.frostbite.a'] = Unexpected_Requests()+Valiant_Crown()
    conf['slots.d'] = Leviathan()
    conf['acl'] = "`rotation"
    conf['rotation'] = """
        s2 s1 dragon end
    """
    coab = ['Blade', 'Tiki', 'Axe2']
    conf['afflict_res.bog'] = 80

    def prerun(self):
        pass

    def s2_before(self, e):
        for _ in range(4):
            Selfbuff('last_bravery',0.3,15).on()
            Event('defchain')()

    def s2_proc(self, e):
        self.dmg_make(f'{e.name}_reflect', 3792*8, fixed=True)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Fjorm, *sys.argv)