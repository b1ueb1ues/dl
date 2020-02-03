import adv_test
import adv
import natalie
from slot.a import HoH, Primal_Crisis
from module import energy
import random

def module():
    return Natalie

class Natalie(natalie.Natalie):
    comment = ''

    def d_slots(this):
        this.slots.a = HoH() + Primal_Crisis()

    def d_acl(this):
        this.conf['acl'] = """
        `s2
        `s1
        `s3, seq=5
        `fs, seq=5 and s1.sp-212<=s1.charged and s1.charged<=s1.sp
    """
    
    def init(this):
        random.seed()
        this.hp = 0
        if this.condition('energy'):
            this.prerun = this.c_prerun

    def prerun(this):
        this.energy = energy.Energy(this,
                self={} ,
                team={} 
                )
        this.a3atk = adv.Selfbuff('a3atk',0.20,-1,'att','passive').on()
        this.a3spd = adv.Spdbuff('a3spd',0.10,-1).on()

    def c_prerun(this):
        this.energy = energy.Energy(this,
                self={'s1':1,'a1':1} ,
                team={}
                )
        this.a3atk = adv.Selfbuff('a3atk',0.20,-1,'att','passive').on()
        this.a3spd = adv.Spdbuff('a3spd',0.10,-1).on()

    def s2_proc(this, e):
        adv.Selfbuff('s2', 0.15, 10).on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2, mass=1)