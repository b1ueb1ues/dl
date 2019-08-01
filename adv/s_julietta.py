import adv_test
from adv import *
from slot.a import *

def module():
    return S_Julietta

class S_Julietta(Adv):
    comment = 'no fs; no bog'
    conf = {}
    conf['slot.a'] = KFM() + CE()

    def init(this):
        this.s2_stance = 1
        this.a3_iscding = 0
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc
        #if this.condition('bog resist 60'):
        #    this.afflics.bog.resist = 60
        #else:
        #    this.afflics.bog.resist = 100

    #def s1_proc(this, e):
    #    r = this.afflics.bog('s1',110)
    #    if r:
    #       Debuff('s1_bog',-0.5*r,8,1,'att','bog').on()

    def s2_proc(this, e):
        if this.s2_stance == 1:
            Selfbuff('s2',0.15,15).on()
            this.s2_stance = 2
        elif this.s2_stance == 2:
            Selfbuff('s2',0.15,15).on()
            Selfbuff('s2',0.10,15, 'crit','chance').on()
            this.s2_stance = 3
        elif this.s2_stance == 3:
            Selfbuff('s2',0.15,15).on()
            Selfbuff('s2',0.10,15, 'crit','chance').on()
            this.s2_stance = 1

    def c_s2_proc(this, e):
        if this.s2_stance == 1:
            Teambuff('s2',0.15,15).on()
            this.s2_stance = 2
        elif this.s2_stance == 2:
            Teambuff('s2',0.15,15).on()
            Teambuff('s2',0.10,15, 'crit','chance').on()
            this.s2_stance = 3
        elif this.s2_stance == 3:
            Teambuff('s2',0.15,15).on()
            Teambuff('s2',0.10,15, 'crit','chance').on()
            this.s2_stance = 1

    def a3_cooldown(this, t):
        this.a3_iscding = 0
        log('cd','a3','end')

    def a3_act(this):
        if not this.a3_iscding :
            this.a3_iscding = 1
            Timer(this.a3_cooldown).on(15)
            log('cd','a3','start')
            Selfbuff('a3',0.10,10).on()
            #Teambuff('db_test',0.10,15).on()
        else:
            log('cd','a3','trigger failed')

    def charge(this, name, sp):
        if this.s1.check():
            return Adv.charge(this, name, sp)
        r = Adv.charge(this, name, sp)
        if this.s1.check():
            this.a3_act()
        return r


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2,seq=4
        `s3,seq=4 
        """
    adv_test.test(module(), conf, verbose=-2)
