import adv_test
import adv
from adv import *
from slot.a import *
from module import energy

def module():
    return B_Zardin

class B_Zardin(adv.Adv):
    a3 = ('s',0.35,'hp70')

    conf = {}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = RR()+BN()
        else:
            this.conf.slot.a = RR()+JotS()
     
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

    if 1:
        module().comment = 'no s2'
        conf['acl'] = """
            `s1
            `s3, seq=5
            """
            #`s2, seq=5 and this.energy() < 4
    else :
        import slot.w
        module().comment = 'with s2 & 4t3'
        conf['slots.w'] = slot.w.blade4b2()
        conf['acl'] = """
            `s3, this.energy() = 5
            `s1
            `s2, seq=5 and this.energy() < 4
            """

    adv_test.test(module(), conf, verbose=0)


