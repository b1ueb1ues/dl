if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return D_Xainfried

class D_Xainfried(Adv):
    conf = {}
    conf['slots.d'] = Freyja()
    conf['slots.a'] = HoH()+A_Dogs_Day()

    def init(this):
        this.a1_iscding = 0
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc

    def c_s1_proc(this, e):
        Teambuff('s1',0.2,15,'crit','chance').on()

    def s1_proc(this, e):
        Selfbuff('s1',0.2,15,'crit','chance').on()

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
            Selfbuff('a1',0.0,10).on()
        else:
            log('cd','a1','trigger failed')

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
        `s2, fsc
        `s3, fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)
