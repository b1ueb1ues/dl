import adv_test
from adv import *
import ramona
from slot.a import *

def module():
    return Ramona

class Ramona(ramona.Ramona):

    def prerun(this):
        this.s1tmp = Conf(this.conf.s1)
        this.a1_iscding = 0
        this.rena_a1_iscding = 0

    def rena_a1_cooldown(this, t):
        this.rena_a1_iscding = 0
        log('cd','rana_a1','end')


    def rena_a1_act(this):
        if not this.rena_a1_iscding :
            this.rena_a1_iscding = 1
            Timer(this.rena_a1_cooldown).on(15)
            log('cd','rana_a1','start')
            Event('defchain')()

    def charge(this, name, sp):
        if this.s1.check():
            return Adv.charge(this, name, sp)
        Adv.charge(this, name, sp)
        if this.s1.check():
            this.a1_act()
            this.rena_a1_act()

    comment = 'with rena in team; '
    conf = {}
    conf['slots.a'] = KFM() + VC()

    conf['acl'] = """
        # s1a = this.s1a
        `s1a
        `s2,seq=4
        `s3,seq=4 
        """



if __name__ == '__main__':
    adv_test.test(module(), conf, verbose=0)