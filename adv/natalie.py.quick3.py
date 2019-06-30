import adv_test
import adv
from adv import *
from module import energy
from slot.d import *
from slot.a import Amulet
import slot

def module():
    return Natalie

class JotS(Amulet):
    att = 64
    a = [('sp',0.08)]

class RR(Amulet):
    att = 64
    a = [('s',0.30)]


class Natalie(adv.Adv):
    conf = {}
    conf['slot.a'] = slot.a.HoH() + slot.a.FoG()
    conf['slot.d'] = Shinobi()
     
    def pre(this):
        if this.condition('energy'):
            this.init = this.c_init

    def init(this):
        this.energy = energy.Energy(this,
                self={} ,
                team={} 
                )

    def c_init(this):
        this.energy = energy.Energy(this,
                self={'s1':1,'a1':1} ,
                team={}
                )
        this.a3atk = Selfbuff('a3atk',0.20,-1,'att','passive').on()
        this.a3spd = Selfbuff('a3spd',0.10,-1,'spd').on()


    def s1_proc(this, e):
        this.energy.add_energy('a1')


if __name__ == '__main__':
    #conf = {}
    #conf['acl'] = """
    #    `s1, this.energy() < 5
    #    `s3, seq=5 and this.energy() = 5
    #    """

    conf = {}
    conf['acl'] = """
        `s1
        `s3, seq=5
        """

    adv_test.test(module(), conf, verbose=-2, mass=0)


