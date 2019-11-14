import adv_test
from adv import *

def module():
    return Yuya

class Yuya(Adv):

    def prerun(this):
        this.a3_iscding = 0
        if this.condition('hp60'):
            Selfbuff('a1',0.2,-1,'att','passive').on()
        else:
            Selfbuff('a1',-0.2,-1,'att','passive').on()

    def s1_proc(this, e):
        Spdbuff("s2",0.2, 10)

    def a3_cooldown(this, t):
        this.a3_iscding = 0
        log('cd','a3','end')

    def a3_act(this):
        #logcat()
        #print this.a3_iscding
        #exit()
        if not this.a3_iscding :
            this.a3_iscding = 1
            Timer(this.a3_cooldown).on(15)
            log('cd','a3','start')
            Selfbuff('a3',0.05,5,'crit','chance').on()
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
        `s3, seq=5
        `fs, seq=5
        """

    #from module import ra
    #ra.test(module(), conf)
    #exit()

    adv_test.test(module(), conf, verbose=0, mass=0)

