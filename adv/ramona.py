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
        this.s1tmp = Conf(this.conf.s1)

    def s1back(this, t):
        this.conf.s1.recovery = this.s1tmp.recovery
        this.conf.s1.dmg = this.s1tmp.dmg

    def s1a(this):
        if this.s1.check():
            this.conf.s1.dmg += 2.93*6
            this.conf.s1.recovery = 6.25
            Timer(this.s1back).on(this.conf.s1.startup+0.01)
            this.hits += 6
            return this.s1()
        else:
            return 0

    def s2_proc(this, e):
       Event('defchain')()



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

