import adv.adv_test
from core.advbase import *
from core.advbase import *
from module import energy
from slot.a import *
from slot.d import *

def module():
    return Pipple

pipple_conf = {
    'x1.dmg': 2.21,
    'x2.dmg': 1.19*2,
    'x3.dmg': 0.80*3,
    'x4.dmg': 1.65*2,
    'x5.dmg': 0.80*4+1.32,
}

class Pipple(Adv):
    conf = pipple_conf.copy()
    conf['slot.a'] = Primal_Crisis()+FirstRate_Hospitality()
    conf['slot.d'] = Leviathan()
    conf['acl'] = """
        `s1, x=5
        `s2, x=5
        """
            
    def init(this):
        if this.condition('energy'):
            this.prerun = this.c_prerun

    def prerun(this):
        this.stance = 0
        this.energy = energy.Energy(this,
                self={} ,
                team={} 
                )
        this.a1atk = Selfbuff('a1atk',0.00,-1,'att','passive').on()
        this.a1crit = Selfbuff('a1crit',0.00,-1,'crit','chance').on()

    def c_prerun(this):
        this.stance = 0
        this.energy = energy.Energy(this,
                self={'1':1,'s2':2},
                team={'1':1,'s2':2}
                )
        this.a1atk = Selfbuff('a1atk',0.00,-1,'att','passive').on()
        this.a1crit = Selfbuff('a1crit',0.00,-1,'crit','chance').on()


    def a3change(this, t):
        this.a1atk.off()
        this.a1crit.off()
        if this.energy() == 5:
            this.a1atk.set(0.40)
            this.a1crit.set(0.15)
        elif this.energy() == 4:
            this.a1atk.set(0.30)
            this.a1crit.set(0.10)
        elif this.energy() == 3:
            this.a1atk.set(0.20)
            this.a1crit.set(0.07)
        elif this.energy() == 2:
            this.a1atk.set(0.10)
            this.a1crit.set(0.04)
        elif this.energy() == 1:
            this.a1atk.set(0.05)
            this.a1crit.set(0.01)
        elif this.energy() == 0:
            this.a1atk.set(0)
            this.a1crit.set(0)
        this.a1atk.on()
        this.a1crit.on()

    def s1_proc(this, e):
        Teambuff('s1', 0.25, 15, 'defense').on()
        if this.stance == 0:
            this.stance = 1
        elif this.stance == 1:
            this.stance = 2
        elif this.stance == 2:
            Timer(this.a3change).on()
            this.stance = 0

    def s2_proc(this, e):
        Timer(this.a3change).on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


