import adv.adv_test
import adv
from adv import *
from slot.a import *
from module import energy
import slot.a
import slot.w

def module():
    return B_Zardin

class B_Zardin(adv.Adv):
    a3 = ('s',0.35,'hp70')

    conf = {}
    comment = 'no s2'
    conf['slots.a'] = RR()+JotS()
    conf['acl'] = """
        `s1
        `s3, seq=5
        """
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = RR()+BN()
     
    def init(this):
        if this.condition('energy'):
            this.prerun = this.c_prerun

    def prerun(this):
        this.energy = energy.Energy(this,
                self={} ,
                team={}
                )

    def c_prerun(this):
        this.energy = energy.Energy(this,
                self={'s1':1,'s2':2} ,
                team={}
                )




if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)


