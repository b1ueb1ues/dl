if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from adv import *
from module import energy
import slot.a
import slot.w

def module():
    return B_Zardin

class B_Zardin(adv.Adv):
    a3 = ('s',0.35,'hp70')

    conf = {}
    comment = 'no s2'
    conf['slots.a'] = slot.a.RR()+slot.a.Jewels_of_the_Sun()
    conf['acl'] = """
        `s1
        """
    # conf['slots.w'] = slot.w.blade4b2()
    def d_slots():
        if this.conf['slots.w'] == slot.w.blade4b2():
            this.comment = 'with s2 & 4t3'
            this.conf['acl'] = """
                `s3, this.energy() = 5
                `s1
                `s2, seq=5 and this.energy() < 4
                """

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
    adv_test.test(module(), conf, verbose=0)


