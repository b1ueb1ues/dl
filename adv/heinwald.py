import adv_test
from adv import *

def module():
    return Heinwald

class Heinwald(Adv):

    def condition(this):
        this.conf['mod_a'] = ('s','passive',0.35)
        this.s2_proc = this.c_s2_proc
        return 'hp70 & buff all teammate'


    def init(this):
        this.charge_p('prep','100%')
        this.s2ssbuff = Buff("s2_shapshifts1",1, 10,'ss','ss','self')


    #def c_s1_proc(this, e):
    #    if this.s2ssbuff.get():
    #        log('-special','s1_with_s2')
    #        Buff('s1teambuff',0.1,10).on()

    #def s1_proc(this, e):
    #    if this.s2ssbuff.get():
    #        log('-special','s1_with_s2')
    #        Buff('s1teambuff',0.1,10,wide='self').on()

    def c_s2_proc(this, e):
        this.s2ssbuff.on()
        Buff('s2team',0.1,10,wide='team').on()
        Buff('s2self',0.1,10,wide='self').on()

    def s2_proc(this, e):
        this.s2ssbuff.on()
        Buff('s2',0.2,10,wide='self').on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf,verbose=0, mass=0)

