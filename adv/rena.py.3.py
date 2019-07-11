import adv_test
from adv import *
from slot.a import *
from slot.d import *


def module():
    return Rena

class Rena(Adv):
    comment = ''
    conf = {}
    conf['slot.d'] = Sakuya()
    conf['slot.a'] = HoH()+FRH()


    def init(this):
        this.a1_iscding = 0

    def s2_proc(this, e):
        this.s1.charge(this.s1.sp)

    def a1_cooldown(this, t):
        this.a1_iscding = 0
        log('cd','a1','end')

    def a1_act(this):
        #logcat()
        #print this.a1_iscding
        #exit()
        if not this.a1_iscding :
            this.a1_iscding = 1
            Timer(this.a1_cooldown).on(15)
            log('cd','a1','start')
            Selfbuff('a1',0.15,10,'def').on()
            Event('defchain')()

    def charge(this, name, sp):
        if this.s1.check():
            return Adv.charge(this, name, sp)
        r = Adv.charge(this, name, sp)
        if this.s1.check():
            this.a1_act()
        return r


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, s=1
        `fs, seq=5 and s1.charged > s1.sp/2
        `s3, fsc or seq=5
        """
    adv_test.test(module(), conf, verbose=0)

