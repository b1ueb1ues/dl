import adv.adv_test
from core.advbase import *
from slot.a import *
from module import energy
import random


def module():
    return S_Luca

class S_Luca(Adv):
    #comment = 'no fs; no bog'
    a1 = ('a',0.1,'hp70')

    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3,seq=4
        `fs, x=5
        """
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = KFM()+HoH()
        else:
            this.conf.slot.a = KFM()+FitF()

    def init(this):
        random.seed()
        if this.condition('energy'):
            this.prerun = this.c_prerun

    def prerun(this):
        this.energy = energy.Energy(this,
                self={} ,
                team={} 
                )

    def c_prerun(this):
        this.energy = energy.Energy(this,
                self={'s2':1,'a3':1} ,
                team={}
                )

    def s2_proc(this, e):
        Spdbuff('s2',0.2,10).on()
        if random.random() < 0.4:
            this.energy.add_energy('a3')



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2, mass=100)
