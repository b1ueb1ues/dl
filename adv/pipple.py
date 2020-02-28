import adv.adv_test
from core.advbase import *
from core.advbase import *
from module import energy
from slot.a import *
from slot.d import *

def module():
    return Pipple

pipple_conf = {
    'xtype': 'ranged',

    'x1.dmg': 2.21,
    'x1.sp': 130,
    'x1.startup': 15/60.0,
    'x1.recovery': 33/60.0,
    'x1.hit': 1,

    'x2.dmg': 1.19*2,
    'x2.sp': 200,
    'x2.startup': 0,
    'x2.recovery': 31/60.0,
    'x2.hit': 2,

    'x3.dmg': 0.80*3,
    'x3.sp': 240,
    'x3.startup': 0,
    'x3.recovery': 53/60.0,
    'x3.hit': 3,

    'x4.dmg': 1.65*2,
    'x4.sp': 430,
    'x4.startup': 0,
    'x4.recovery': 64/60.0,
    'x4.hit': 2,

    'x5.dmg': 0.80*4+1.32,
    'x5.sp': 600,
    'x5.startup': 0,
    #'x5.recovery': 68/60.0,
    'x5.recovery': 29/60.0,
    'x5.hit': 5,

    'fs._startup': 0,
    'fs._recovery': 29/60.0,

    'fs.dmg': 0.9*2,
    'fs.sp': 400,
    'fs.startup': 43 / 60.0, # 30f for 2nd hit not considered
    'fs.recovery': 46 / 60.0,
    'fs.hit': 2,

    'x1fs.startup': 54 / 60.0, # 11 delay + fs
    'x2fs.startup': 50 / 60.0, # 7 delay + fs

    'dodge.startup': 36 / 60.0,
    'dodge.recovery': 0 / 60.0,

    'missile_iv': {
        #'fs': 0.7/2,
        #'x1': 0.7,
        #'x2': 0.7,
        #'x3': 0.7,
        #'x4': 0.7,
        #'x5': 0.7,
        'fs': 0,
        'x1': 0,
        'x2': 0,
        'x3': 0,
        'x4': 0,
        'x5': 0,
    },
}

class Pipple(Adv):
    conf = pipple_conf.copy()
    conf['slot.a'] = PC()+The_Prince_of_Dragonyule()
    conf['slot.d'] = Leviathan()
    conf['acl'] = """
        `dragon, x=5
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
        if this.stance == 0:
            this.stance = 1
        elif this.stance == 1:
            this.stance = 2
        elif this.stance == 2:
            this.energy.add_energy('1')
            Timer(this.a3change).on()
            this.stance = 0

    def s2_proc(this, e):
        Timer(this.a3change).on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


