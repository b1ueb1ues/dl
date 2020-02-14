import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return S_Ranzal

class S_Ranzal(Adv):
    a1 = ('lo',0.4)
    a3 = ('primed_def', 0.08)

    conf = {}
    conf['slot.a'] = RR() + FRH()
    conf['acl'] = """
        `s1, x=5
        `s2, x=5
        `s3, x=5
        """
    conf['afflict_res.bog'] = 100

    def init(this):
        this.a3_iscding = 0
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc

    def s1_proc(this, e):
        this.dmg_make('s1',2.16)
        this.afflics.bog.on('s1', 100)
        this.dmg_make('s1',6.48)

    def c_s2_proc(this, e):
        Teambuff('s2',0.10,15).on()

    def s2_proc(this, e):
        Selfbuff('s2',0.10,15).on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)
