import adv_test
from adv import *
from slot.d import *
from slot.a import *
from module import energy

def module():
    return G_Elisanne

class G_Elisanne(Adv):

    conf = {}
    conf['slots.a'] = BB()+FWHC()
    conf['slots.d'] = H_Maritimus()
    
    def init(this):
        this.a3_iscding = 0
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc
        if this.condition('energy'):
            this.prerun = this.c_prerun
        this.s2timer = Timer(this.s2autocharge,1,1).on()

    def c_prerun(this):
        this.stance = 0
        this.energy = energy.Energy(this, 
                self={},
                team={}
                )

    def c_prerun(this):
        this.stance = 0
        this.energy = energy.Energy(this, 
                self={'s2':3},
                team={}
                )

    def s2autocharge(this, t):
        this.s2.charge(38400.0*0.065)
        log('sp','s1autocharge')

    def c_s1_proc(this, e):
        Teambuff('s2',0.3,15).on()

    def s1_proc(this, e):
        Selfbuff('s2',0.3,15).on()

    def a3_cooldown(this, t):
        this.a3_iscding = 0
        log('cd','a3','end')

    def a3_act(this):
        #logcat()
        #print this.a1_iscding
        #exit()
        if not this.a3_iscding :
            this.a3_iscding = 1
            Timer(this.a3_cooldown).on(15)
            log('cd','a3','start')
            Selfbuff('a3',0.0,10,'str').on()
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
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)

