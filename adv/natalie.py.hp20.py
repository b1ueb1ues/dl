import adv_test
import adv
from adv import *
from module import energy
from slot.d import *
from slot.a import Amulet
import slot
import random

def module():
    return Natalie

class JotS(Amulet):
    att = 64
    a = [('sp',0.08)]

class RR(Amulet):
    att = 64
    a = [('s',0.30)]


class Natalie(adv.Adv):
    comment = '20hp; 120s; can\'t maintain comboes'
    conf = {}
    conf['slot.a'] = slot.a.TL() + slot.a.Choco()
    conf['slot.d'] = Shinobi()
     
    def init(this):
        random.seed()
        this.crisis = 0
        if this.condition('energy'):
            this.prerun = this.c_prerun
        if this.condition('hp20'):
            this.crisis = 1*0.8*0.8

    def prerun(this):
        this.energy = energy.Energy(this,
                self={} ,
                team={} 
                )

    def c_prerun(this):
        this.energy = energy.Energy(this,
                self={'s1':1,'a1':1} ,
                team={}
                )
        this.a3atk = Selfbuff('a3atk',0.20,-1,'att','passive').on()
        this.a3spd = Spdbuff('a3spd',0.10,-1).on()


    def s1_proc(this, e):
        if this.crisis > 0:
            this.dmg_make('o_s1_crisis', this.crisis*10.62)
            if this.energy() == 5:
                this.dmg_make('o_s1_crisis_energized', this.crisis*10.62*this.energy.get_energy_boost())
        if random.random() < 0.8:
            this.energy.add_energy('a1')

    def s2_proc(this, e):
        Selfbuff('s2str',0.15,10).on()





if __name__ == '__main__':
    #conf = {}
    #conf['acl'] = """
    #    `s1, this.energy() < 5
    #    `s3, seq=5 and this.energy() = 5
    #    """

    conf = {}
    conf['acl'] = """
        `s2
        `s1
        `s3, seq=5
        `fs, seq=5 and s1.sp-212<=s1.charged and s1.charged<=s1.sp
        """
 #   conf['acl'] = """
 #       `s2, pin='prep'
 #       `s2, seq=5
 #       `s1
 #       `s3, fsc
 #       `s3, seq=5 and s1.charged < s1.sp-200
 #       `fs, seq=5 and s1.sp-212<=s1.charged and s1.charged<=s1.sp
 #       `fs, seq=5 and s1.sp > 3000 and s3.charged>=s3.sp
 #       """


    adv_test.test(module(), conf, verbose=-2, mass=1,duration=120)


