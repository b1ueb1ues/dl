import adv_test
import adv
from adv import *
from module import energy

def module():
    return B_Zardin

class B_Zardin(adv.Adv):
    a3 = ('s',0.35,'hp70')
     
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
                self={'s1':1,'s2':2} ,
                team={}
                )




if __name__ == '__main__':
    conf = {}
    from slot.a import *

    if 1:
        module().comment = 'no s2'
        conf['slots.a'] = RR()+Jewels_of_the_Sun()
        conf['acl'] = """
            `s1
            """
            #`s2, seq=5 and this.energy() < 4
    else :
        import slot.w
        module().comment = 'no s2 & 4t3'
        conf['slots.w'] = slot.w.blade4b2()
        conf['slots.a'] = HoH() + CE()  
        conf['acl'] = """
            `s3, this.energy() = 5
            `s1
            `s2, seq=5 and this.energy() < 4
            """

    adv_test.test(module(), conf, verbose=0)


