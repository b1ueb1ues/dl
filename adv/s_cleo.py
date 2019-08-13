import adv_test
import adv
from adv import *
import slot
from slot.a import *

def module():
    return S_Cleo

class S_Cleo(Adv):
    a3 = ('k_paralysis',0.3)
    conf = {}
    comment = 'nofs'

    def init(this):
        this.bc = Selfbuff()
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc

        this.conf['acl'] = """
            `s3
            `s2,s1.charged>=s1.sp
            `s1
            """

        #if this.condition('c4+fs'):
        #    this.conf['acl'] = """
        #        `s3,s1.charged>=s1.sp
        #        `s2
        #        `s1
        #        `fs, seq=4
        #        """
        #else:
        #    this.conf['acl'] = """
        #        `s3,s1.charged>=s1.sp
        #        `s2
        #        `s1
        #        """

    def s1_proc(this, e):
        this.dmg_make('s1_missile',1.06)
        this.afflics.paralysis('s1',100,0.66)
        buffcount = this.bc.buffcount()
        Selfbuff('a1',0.10*this.afflics.paralysis.get(),20,'sp','passive').on()
        this.dmg_make('s1_missile',1.06)
        this.dmg_make('s1_missile',1.06)
        this.dmg_make('s1_big_missile',5.3)

        if buffcount > 4:
            buffcount = 4
        for i in range(buffcount):
            this.dmg_make('o_s1_boost',1.06)

    def c_s2_proc(this, e):
        Teambuff('s2str',0.05,10).on()
        Teambuff('s2crit',0.03,10,'crit','chance').on()
        Teambuff('s2sd',0.10,10,'s').on()
        Teambuff('s2sp',0.20,10,'sp','passive').on()

    def s2_proc(this, e):
        Selfbuff('s2str',0.05,10).on()
        Selfbuff('s2crit',0.03,10,'crit','chance').on()
        Selfbuff('s2sd',0.10,10,'s').on()
        Selfbuff('s2sp',0.20,10,'sp','passive').on()


if __name__ == '__main__':
    conf = {}

    adv_test.test(module(), conf, verbose=-2)

