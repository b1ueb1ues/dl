import adv_test
from adv import *
from slot.d import *
from slot.a import *
from module import energy


def module():
    return Noelle

class Noelle(Adv):
    a1 = ('bt',0.25)

    conf = {}
    conf['slots.d'] = Freyja()
    conf['slots.a'] = HG()+FWHC()


    def init(this):
        energy.Energy(this,{},{})
        this.a1_iscding = 0
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc


    def c_s1_proc(this, e):
        Teambuff('s2',0.25,15).on()

    def s1_proc(this, e):
        Selfbuff('s2',0.25,15).on()

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
    conf['acl'] = """
        `s1
        `s2, fsc
        `s3, fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)

