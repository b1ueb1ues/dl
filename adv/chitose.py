import adv_test
from adv import *
from slot.d import *
from slot.a import *

def module():
    return Chitose

class Chitose(Adv):
    a3 = ('a',-0.1)

    conf = {}
    conf['slot.a'] = HG()+FWHC()
    conf['slot.d'] = Daikokuten()

    def init(this):
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc

    def c_s1_proc(this, e):
        Teambuff('s1',0.25,15).on()

    def s1_proc(this, e):
        Selfbuff('s1',0.25,15).on()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3, fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)

