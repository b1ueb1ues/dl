import adv.adv_test
from core.advbase import *
from module import energy
from slot.d import *
from slot.a import *
import slot
import random

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

    def d_slots(this):
        from adv.adv_test import sim_duration
        if sim_duration <= 60:
            this.slots.a = TL()+The_Chocolatiers()

    def init(this):
        random.seed()
        if this.condition('energy'):
            this.prerun = this.c_prerun

    def prerun(this):
        this.hp = 100
        this.a3atk = Selfbuff('a3atk',0.20,-1,'att','passive')
        this.a3spd = Spdbuff('a3spd',0.10,-1)
        this.energy = energy.Energy(this,
                self={} ,
                team={}
                )

    def c_prerun(this):
        this.hp = 100
        this.a3atk = Selfbuff('a3atk',0.20,-1,'att','passive')
        this.a3spd = Spdbuff('a3spd',0.10,-1)
        this.energy = energy.Energy(this,
                self={'s1':1,'a1':1} ,
                team={}
                )


    def s1_proc(this, e):
        with CrisisModifier('s1', 1, this.hp):
            this.dmg_make('s1', 10.62)

        if random.random() < 0.8:
            this.energy.add_energy('a1')

    def s2_proc(this, e):
        if this.hp > 30:
            this.hp = 20
            this.a3atk.on()
            this.a3spd.on()
        else:
            Selfbuff('s2', 0.15, 10).on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2, mass=1)


