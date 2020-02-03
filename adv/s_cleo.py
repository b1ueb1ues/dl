import adv.adv_test
import adv
from adv import *
import slot
from slot.a import *
from slot.d import *

def module():
    return S_Cleo

class S_Cleo(Adv):
    a3 = ('k_paralysis',0.3)
    conf = {}
    conf['slot.d'] = Corsaint_Phoenix()
    comment = 'nofs'
    conf['cond_afflict_res'] = 0
    conf['acl'] = """
            `s2
            `s1
            `s3
            """
    def init(this):
        random.seed()
        this.bc = Selfbuff()
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc

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
    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.paralysis.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.paralysis.resist=100


    def s1_lantency(this, t):
        this.dmg_make('s1_missile',1.06)
        this.hits += 1
        p = this.afflics.paralysis('s1',120,0.97)
        buffcount = this.bc.buffcount()
        this.afflics.paralysis.get()
        if random.random() < p :
            Selfbuff('a1',0.10,20,'sp','passive').on()
        this.dmg_make('s1_missile',1.06)
        this.hits += 1
        this.dmg_make('s1_missile',1.06)
        this.hits += 1
        this.dmg_make('s1_big_missile',5.3)
        this.hits += 1

        if buffcount > 4:
            buffcount = 4
        for i in range(buffcount):
            this.dmg_make('o_s1_boost',1.06)
            this.hits += 1

    def s1_proc(this, e):
        Timer(this.s1_lantency).on(1)

    def c_s2_proc(this, e):
        Teambuff('s2str',0.05,10).on()
        Teambuff('s2crit',0.03,10,'crit','chance').on()
        Teambuff('s2sd',0.10,10,'s').on()
        Teambuff('s2sp',0.10,10,'sp','passive').on()

    def s2_proc(this, e):
        Selfbuff('s2str',0.05,10).on()
        Selfbuff('s2crit',0.03,10,'crit','chance').on()
        Selfbuff('s2sd',0.10,10,'s').on()
        Selfbuff('s2sp',0.10,10,'sp','passive').on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2, mass=100)

