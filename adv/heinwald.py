import adv.adv_test
from adv import *
from slot.a.all import *
from slot.d import *

def module():
    return Heinwald

class Heinwald(Adv):
    a1 = ('s',0.35)
    conf = {}
    conf['slots.a'] = RR()+JotS()

    def init(this):
        if this.condition("buff all teammates"):
            this.s2_proc = this.c_s2_proc


    def prerun(this):
        this.charge_p('prep','100%')
        this.s2ssbuff = Selfbuff("s2_shapshifts1",1, 10,'ss','ss')


    def c_s2_proc(this, e):
        this.s2ssbuff.on()
        Teambuff('s2team',0.1,10).on()
        Selfbuff('s2self',0.1,10).on()

    def s2_proc(this, e):
        this.s2ssbuff.on()
        Selfbuff('s2',0.2,10).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3
        """
    adv_test.test(module(), conf,verbose=0, mass=0)

