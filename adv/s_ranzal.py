import adv_test
from adv import *
from slot.a import *

def module():
    return S_Ranzal

class S_Ranzal(Adv):
    comment = 'no bog'

    conf = {}
    conf['slot.a'] = RR() + FRH()

    a1 = ('lo',0.4)

    def init(this):
        this.a3_iscding = 0
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc
       # if this.condition('bog resist 60'):
       #     this.afflics.bog.resist = 60
       # else:
       #     this.afflics.bog.resist = 100

    #def s1_proc(this, e):
    #    r = this.afflics.bog('s1',100)
    #    if r:
    #       Debuff('s1_bog',-0.5*r,8,1,'att','bog').on()


    def c_s2_proc(this, e):
        Teambuff('s2',0.10,15).on()

    def s2_proc(this, e):
        Selfbuff('s2',0.10,15).on()

    def a3_cooldown(this, t):
        this.a3_iscding = 0
        log('cd','a3','end')

    def a3_act(this):
        if not this.a3_iscding :
            this.a3_iscding = 1
            Timer(this.a3_cooldown).on(15)
            log('cd','a3','start')
            Selfbuff('a3',0.0,10,'def').on()
            #Teambuff('db_test',0.10,15).on()
            Event('defchain')()
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
        `s1, x=5
        `s2, x=5
        """
    adv_test.test(module(), conf, verbose=-2)
