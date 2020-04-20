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
        `s2, x=5
        """
    coab = ['Ieyasu','Curran','Berserker']

    def prerun(self):
        # Teambuff('last',2.28,1).on()
        self.hp = 100
        self.a1_buff = Selfbuff('a1', 0.30, -1, 's', 'buff')

    def s1_proc(self, e):
        with CrisisModifier('s1', 0.5, self.hp), KillerModifier('s1_killer', 'hit', 0.2, ['poison']):
            self.dmg_make('s1', 19.05)
        if self.hp >= 50:
            self.hp -= 10
            self.charge_p('s1_hpcut', 0.20, target='s1')
            # assume you take bit more damage at and proc last destruction at some point
            if self.hp <= 50:
                self.hp = 40
                self.a1_buff.on()

    def s2_proc(self, e):
        self.hp += 23


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)