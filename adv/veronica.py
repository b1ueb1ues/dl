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
        `dragon.act("c3 s end"), s
        `s3, not self.s3_buff
        `s1
        `s4
        """
    coab = ['Ieyasu','Curran','Summer_Patia']
    share = ['Curran']

    def prerun(self):
        # Teambuff('last',2.28,1).on()
        self.a1_buff = Selfbuff('a1', 0.30, -1, 's', 'buff')
        Event('hp').listener(self.a1_buff_on)

    def a1_buff_on(self, e):
        # assume you take bit more damage at and proc last destruction at some point
        if e.hp <= 50 and not self.a1_buff.get():
            self.set_hp(30)
            self.a1_buff.on()

    def s1_proc(self, e):
        with CrisisModifier(e.name, 0.5, self.hp), KillerModifier('s1_killer', 'hit', 0.2, ['poison']):
            self.dmg_make(e.name, 19.05)
        if self.hp >= 50:
            self.set_hp(self.hp-10)
            self.charge_p(f'{e.name}_hpcut', 0.20, target=e.name)

    def s2_proc(self, e):
        self.set_hp(self.hp+7.7)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
