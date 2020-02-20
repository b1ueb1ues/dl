import adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Delphi

class Delphi(Adv):
    a1 = ('a',-0.6)

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.poison.resist=0
        else:
            this.afflics.poison.resist=100

        if this.condition('hit15'):
            this.proc_chance = 180
        else:
            this.proc_chance = 120
        
        if this.condition('s1 defdown for 10s'):
            this.s1defdown = 1
        else:
            this.s1defdown = 0
        
        this.skilltimer = Timer(this.skillautocharge,1,1).on()
        this.s1fscharge = 0

    def skillautocharge(this, t):
        this.s1.charge(999999.0*0.08)
        this.s2.charge(999999.0*0.05)
        log('sp','s1autocharge')

    def s1_proc(this, e):
        if this.s1defdown :
            Debuff('s1defdown',0.15,10,1).on()
        this.s1fscharge = 1

    def s2_proc(this, e):
        this.afflics.poison('s2',120,3.00,24)

    def fs_proc(this, e):
        if this.s1fscharge > 0:
            this.s1fscharge -= 1
            this.dmg_make("o_fs_boost",0.21*3)
            this.afflics.poison('fs',this.proc_chance,3.00,24)

if __name__ == '__main__':
    conf = {}
    conf['slots.a'] = TB()+SDO()
    conf['slot.d'] = Marishiten()
    conf['acl'] = """
        `s1
        `s3
        `fs,seq=2 and cancel
    """

    adv.adv_test.test(module(), conf)
