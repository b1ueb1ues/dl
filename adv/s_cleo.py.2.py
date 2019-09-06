import adv_test
import adv
from adv import *
import slot
from slot.a import *
import s_cleo

def module():
    return S_Cleo

class S_Cleo(s_cleo.S_Cleo):
    def init(this):
        random.seed()
        this.bc = Selfbuff()
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc

        this.conf['acl'] = """
            `s2, s1.charged>=s1.sp
            `s1
            `s3
            """


if __name__ == '__main__':
    conf = {}
    conf['slot.a'] = HoH() + JotS()

    adv_test.test(module(), conf, verbose=-2, mass=100)

