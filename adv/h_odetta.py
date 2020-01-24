import adv_test
from adv import *
from slot.a import *
from slot.d import *
from slot.w import *

def module():
    return H_Odetta

class H_Odetta(Adv):

    conf = {}
    conf['slot.a'] = MF() + FRH()
    conf['slot.d'] = DJ()

    a1 = ('primed_def', 0.10)
    a3 = ('bt',0.2)

    def init(this):
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc

    def c_s2_proc(this, e):
        Teambuff('s2',0.2,15).on()

    def s2_proc(this, e):
        Selfbuff('s2',0.2,15).on()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, fsc
        `s1, fsc
        `s3, fsc
        `fs, seq=2
        """
    adv_test.test(module(), conf, verbose=-2)
