if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.d import *
from slot.a import *
from module import energy

def module():
    return Emma

class Emma(Adv):
    a1 = ('bt',0.25)

    conf = {}
    conf['slots.d'] = Cerberus()
    conf['slot.a'] = HG()+BB()
    conf['acl'] = """
                `s1
                `s3, fsc
                `fs, seq=5
                """

    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = HG()+JotS()
            this.conf['acl'] = """
                        `s1
                        `s3, seq=5
                        """

    def init(this):
        comment = 'no s2'
        energy.Energy(this,{},{})
        this.a3_iscding = 0
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc


    def c_s1_proc(this, e):
        Teambuff('s2',0.25,15).on()

    def s1_proc(this, e):
        Selfbuff('s2',0.25,15).on()

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
    adv_test.test(module(), conf, verbose=-2)

