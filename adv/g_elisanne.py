if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.d import *
from slot.a import *
from module import energy

def module():
    return G_Elisanne

class G_Elisanne(Adv):
    a3 = ('primed_att',0.10)

    conf = {}
    conf['slots.a'] = BB()+FWHC()
    conf['slots.d'] = H_Maritimus()
    conf['acl'] = """
        `s1
        `fs, seq=5
        """

    def init(this):
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc
        if this.condition('energy'):
            this.prerun = this.c_prerun
        this.s2timer = Timer(this.s2autocharge,1,1).on()

    def c_prerun(this):
        this.stance = 0
        this.energy = energy.Energy(this, 
                self={},
                team={}
                )

    def c_prerun(this):
        this.stance = 0
        this.energy = energy.Energy(this, 
                self={'s2':3},
                team={}
                )

    def s2autocharge(this, t):
        this.s2.charge(38400.0*0.065)
        log('sp','s1autocharge')

    def c_s1_proc(this, e):
        Teambuff('s2',0.3,15).on()

    def s1_proc(this, e):
        Selfbuff('s2',0.3,15).on()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

