import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Ramona

class Ramona(Adv):
    comment = 'no fs'
    a3 = ('bc',0.13)
    conf = {}
    conf['slots.a'] = KFM()+VC()
    #conf['slots.a'] = KFM()+TL()
    conf['slots.d'] = Sakuya()

    def prerun(this):
        this.s1tmp = Conf(this.conf.s1)
        this.a1_iscding = 0

    def s1back(this, t):
        this.conf.s1.recovery = this.s1tmp.recovery
        this.conf.s1.dmg = this.s1tmp.dmg

    def s1a(this):
        if this.s1.check():
            this.conf.s1.dmg += 2.93*6
            this.conf.s1.recovery = 6.25
            Timer(this.s1back).on(this.conf.s1.startup+0.01)
            return this.s1()
        else:
            return 0

    def s2_proc(this, e):
       Event('defchain')()

    def a1_cooldown(this, t):
        this.a1_iscding = 0
        log('cd','a1','end')


    def a1_act(this):
        if not this.a1_iscding :
            this.a1_iscding = 1
            Timer(this.a1_cooldown).on(15)
            log('cd','a1','start')
            Selfbuff('a1',0.1,10).on()

    def charge(this, name, sp):
        if this.s1.check():
            return Adv.charge(this, name, sp)
        Adv.charge(this, name, sp)
        if this.s1.check():
            this.a1_act()




if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        # s1a = this.s1a
        `s1a
        `s2,seq=4
        `s3,seq=4 
        """
        
    import sys
    from slot.a import *
    if len(sys.argv) >= 3:
        sim_duration = int(sys.argv[2])
    else:
        sim_duration = 180
    if sim_duration == 60:
        module().comment += ';TL>EoL>CE>VC if trigger'
    elif sim_duration == 90:
        module().comment += ';TL>EoL>CE>VC if trigger'
    elif sim_duration == 120:
        module().comment += ';TL>EoL>VC>CE if trigger'
    elif sim_duration == 180:
        module().comment += ';EoL>TL>VC>CE if trigger'

    adv_test.test(module(), conf, verbose=0)

