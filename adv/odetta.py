import adv.adv_test
from adv import *
from slot.a import *

def module():
    return Odetta

class Odetta(Adv):
    comment = 'c2+fs'

    conf = {}
    conf['slot.a'] = RR() + Stellar_Show()

    a1 = ('a',0.1,'hp70')
    a3 = ('bt',0.2)

    def init(this):
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc

    def c_s2_proc(this, e):
        Teambuff('s2',0.15,15).on()

    def s2_proc(this, e):
        Selfbuff('s2',0.15,15).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, fsc
        `s1, fsc
        `fs, seq=2
        """
    adv_test.test(module(), conf, verbose=-2)
