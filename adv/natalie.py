from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Natalie

class Natalie(Adv):
    conf = {}
    conf['slots.a'] = HoH() + Dear_Diary()
    conf['slots.poison.a'] = HoH() + The_Plaguebringer()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s2, s=3 or x=5
        `s1
        """
    coab = ['Wand','Curran','Berserker']

    def d_slots(self):
        if self.duration <= 60:
            self.conf['slots.a'] = The_Chocolatiers()+TL()
            self.conf['slots.poison.a'] = The_Chocolatiers()+The_Plaguebringer()

    def prerun(self):
        self.a3atk = Selfbuff('a3atk',0.20,-1,'att','passive')
        self.a3spd = Spdbuff('a3spd',0.10,-1)

    def s1_proc(self, e):
        with CrisisModifier(e.name, 1, self.hp):
            self.dmg_make(e.name, 10.62)

        self.energy.add(1.8)
        # self.energy.add(1)
        # if random.random() < 0.8:
        #     self.energy.add(1)

    def s2_proc(self, e):
        if self.hp > 30:
            self.set_hp(20)
            self.a3atk.on()
            self.a3spd.on()
        else:
            Selfbuff(e.name, 0.15, 10).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)