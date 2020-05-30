from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Veronica

class Veronica(Adv):
    comment = 'last destruction team DPS not considered'
    a3 = [('prep',1.00), ('scharge_all', 0.05)]
    conf = {}
    conf['slots.a'] = Candy_Couriers()+Primal_Crisis()
    conf['slots.poison.a'] = Candy_Couriers()+The_Plaguebringer()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2, x=5 and self.a1_buff.get() and self.hp<50
        """
    coab = ['Ieyasu','Curran','Berserker']

    def prerun(self):
        # Teambuff('last',2.28,1).on()
        self.a1_buff = Selfbuff('a1', 0.30, -1, 's', 'buff')

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.a1_buff = Dummy()

    def s1_proc(self, e):
        with CrisisModifier(e.name, 0.5, self.hp), KillerModifier('s1_killer', 'hit', 0.2, ['poison']):
            self.dmg_make(e.name, 19.05)
        if self.hp >= 50:
            self.set_hp(self.hp-10)
            self.charge_p(f'{e.name}_hpcut', 0.20, target=e.name)
            # assume you take bit more damage at and proc last destruction at some point
            if self.hp <= 50:
                self.a1_buff.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
