import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
from slot.w import *


def module():
    return Rena

class Rena(Adv):
    a1 = ('primed_defense',0.08)

    conf = {}
    conf['slot.d'] = Sakuya()
    conf['slot.a'] = RR()+Elegant_Escort()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1
        `s2, s=1
        `fs, seq=5 and (s1.charged=1500 or s1.charged=3200)
        """
    conf['afflict_res.burn'] = 0

    def prerun(this):
        this.stance = 0

    def s1_proc(this, e):
        if this.stance == 0:
            this.stance = 1
            this.dmg_make("s1", 0.72)
            this.hits += 1
            this.afflics.burn('s1',120,0.97)
            this.dmg_make("s1", 8.81)
            this.hits += 4

        elif this.stance == 1:
            this.stance = 2
            this.dmg_make("s1", 0.72)
            this.afflics.burn('s1',120,0.97)
            this.hits += 1
            this.dmg_make("s1", 8.81)
            Selfbuff('s1crit',0.1,15,'crit','chance').on()
            this.hits += 4

        elif this.stance == 2:
            this.stance = 0
            with Modifier("s1killer", "burn_killer", "hit", 0.8):
                this.dmg_make("s1", 0.72)
                this.hits += 1
                this.afflics.burn('s1',120,0.97)
                this.dmg_make("s1", 8.81)
                this.hits += 4
            Selfbuff('s1crit',0.1,15,'crit','chance').on()


    def s2_proc(this, e):
        this.s1.charge(this.s1.sp)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
    #logcat(['cd'])
