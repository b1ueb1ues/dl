import adv_test
import adv
from adv import *

def module():
    return Renee

class Renee(adv.Adv):
    def pre(this):
        if this.condition('bog<=3'):
            this.o_init = this.init
            this.init = this.c_init

    def init(this):
        this.a1_iscding = 0
        this.bogcountlast = 0
        this.bogbuff = adv.Debuff('s2_bog',-0.5,8,1,'att','bog')


    def c_init(this):
        this.o_init()
        this.bogcountlast = 3

    def s1_proc(this, e):
        if this.bogcountlast > 0:
            if not this.bogbuff.get():
                this.bogcountlast -= 1
                this.bogbuff.on()

    def a1_cooldown(this, t):
        this.a1_iscding = 0
        log('cd','a1','end')


    def a1_act(this):
        if not this.a1_iscding :
            this.a1_iscding = 1
            Timer(this.a1_cooldown).on(15)
            log('cd','a1','start')
            Selfbuff('a1',0.06,5,'crit','chance').on()

    def charge(this, name, sp):
        if this.s1.check():
            return Adv.charge(this, name, sp)
        Adv.charge(this, name, sp)
        if this.s1.check():
            this.a1_act()




if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)

