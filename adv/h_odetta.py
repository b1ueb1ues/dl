if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *
from slot.w import *

def module():
    return H_Odetta

class H_Odetta(Adv):
    comment = 'c2+fs'

    conf = {}
    conf['slot.a'] = VC() + SS()
    conf['slot.d'] = DJ()
    conf['acl'] = """
        `s2, fsc
        `s1, fsc
        `s3, fsc
        `fs, seq=2
        """

    a3 = ('bt',0.2)

    def init(this):
        this.a1_iscding = 0
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc

    def c_s2_proc(this, e):
        Teambuff('s2',0.2,15).on()

    def s2_proc(this, e):
        Selfbuff('s2',0.2,15).on()

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
            Selfbuff('a1',0.0,10,'def').on()
            #Teambuff('db_test',0.10,15).on()
            Event('defchain')()
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
    adv_test.test(module(), conf, verbose=-2)
