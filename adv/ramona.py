import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Ramona

class Ramona(Adv):
    a1 = ('primed_att',0.10)
    a3 = ('bc',0.13)
    conf = {}
    conf['slots.a'] = KFM()+VC()
    conf['slots.d'] = Sakuya()
    conf['acl'] = """
        `s3, not this.s3_buff
        `s1a
        `s2,seq=4
        """

    def prerun(this):
        this.a_s1 = this.s1.ac
        this.a_s1a = S('s1', Conf({'startup': 0.10, 'recovery': 3.10}))
        def recovery():
            return this.a_s1a._recovery + this.a_s1.getrecovery()
        this.a_s1a.getrecovery = recovery

    def s1back(this, t):
        this.s1.ac = this.a_s1

    def s1a(this):
        if this.s1.check():
            this.dmg_make('s1', 2.93*6)
            this.hits += 6
            this.s1.ac = this.a_s1a
            Timer(this.s1back).on(this.conf.s1.startup+0.01)
            return this.s1()
        else:
            return 0

    def s2_proc(this, e):
       Event('defchain')()



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

