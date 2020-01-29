if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a.all import *
from slot.d import *

def module():
    return Heinwald

class Heinwald(Adv):
    a1 = ('s',0.4,'hp70')
    a3 = ('prep_charge','5%')

    conf = {}
    conf['slots.a'] = RR()+Primal_Crisis()
    conf['acl'] = """
        `s2, pin='prep'
        `s2, seq=5
        `s1, seq=5 or s=2
        `s3
        """

    def init(this):
        if this.condition("buff all teammates"):
            this.s2_proc = this.c_s2_proc

    def prerun(this):
        this.s2ssbuff = Selfbuff("s2_shapshifts1",1, 10,'ss','ss')
        
    def c_s2_proc(this, e):
        this.s2ssbuff.on()
        Teambuff('s2team',0.15,10).on()
        Selfbuff('s2self',0.10,10).on()

    def s2_proc(this, e):
        this.s2ssbuff.on()
        Selfbuff('s2',0.25,10).on()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf,verbose=0, mass=0)

