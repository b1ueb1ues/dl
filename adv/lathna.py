import adv_test
from adv import *
from slot.a import *

from slot.d import *


def module():
    return Lathna

class Lathna(Adv):
    comment = 'no poison'
    conf = {}
    conf['slot.a'] = RR()+BN()
    conf['acl'] = """
        # s1a = this.s1a
        `s1a
        `s2, seq = 5
        `s3, seq = 5
        """

    def prerun(this):
        this.s1tmp = Conf(this.conf.s1)

    def s1back(this, t):
        this.conf.s1.recovery = this.s1tmp.recovery
        this.conf.s1.dmg = this.s1tmp.dmg

    def s1a(this):
        if this.s1.check():
            this.conf.s1.dmg += 1.58*4

            if this.afflics.poison.get():
                coef = 1.975*4
                this.dmg_make("o_s1_boost", coef)
            this.conf.s1.recovery = 4.05
            Timer(this.s1back).on(this.conf.s1.startup+0.01)
            return this.s1()
        else:
            return 0 
    
    def s1_proc(this, e):
        if this.afflics.poison.get():
            coef = 1.975*3
            this.dmg_make("o_s1_boost", coef)


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

