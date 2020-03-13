from core.advbase import *
from slot.d import *
from slot.a import *
import slot

def module():
    return Natalie

class Natalie(Adv):
    conf = {}
    conf['slot.a'] = HoH() + Dear_Diary()
    conf['slot.d'] = Shinobi()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s2, s=3 or x=5
        `s1
        """

    def d_slots(self):
        if self.duration <= 60:
            self.slots.a = TL()+The_Chocolatiers()

    def prerun(self):
        self.hp = 100
        self.a3atk = Selfbuff('a3atk',0.20,-1,'att','passive')
        self.a3spd = Spdbuff('a3spd',0.10,-1)

    def s1_proc(self, e):
        with CrisisModifier('s1', 1, self.hp):
            self.dmg_make('s1', 10.62)

        self.energy.add(1.8)
        # self.energy.add(1)
        # if random.random() < 0.8:
        #     self.energy.add(1)

    def s2_proc(self, e):
        if self.hp > 30:
            self.hp = 20
            self.a3atk.on()
            self.a3spd.on()
        else:
            Selfbuff('s2', 0.15, 10).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)