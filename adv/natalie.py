import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *
import slot

def module():
    return Natalie

class Dear_Diary(Dear_Diary_Slow_RO):
    att = 65

class Natalie(Adv):
    comment = 's2 without str buff'
    conf = {}
    conf['slot.a'] = HoH() + Dear_Diary()
    conf['slot.d'] = Shinobi()
    conf['acl'] = """
        `s2, pin='prep'
        `s2, seq=5
        `s1
        `s3, fsc
        `s3, seq=5 and s1.charged < s1.sp-200
        `fs, seq=5 and s1.sp-212<=s1.charged and s1.charged<=s1.sp
        `fs, seq=5 and s1.sp > 3000 and s3.charged>=s3.sp
        """

    def d_slots(self):
        from adv.adv_test import sim_duration
        if sim_duration <= 60:
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
    conf = {}
    adv.adv_test.test(module(), conf)


