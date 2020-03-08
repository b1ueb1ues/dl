import adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Delphi

class Delphi(Adv):
    a1 = ('a',-0.6)

    def prerun(self):
        if self.condition('0 resist'):
            self.afflics.poison.resist=0
        else:
            self.afflics.poison.resist=100

        if self.condition('hit15'):
            self.proc_chance = 180
        else:
            self.proc_chance = 120
        
        if self.condition('s1 defdown for 10s'):
            self.s1defdown = 1
        else:
            self.s1defdown = 0
        
        self.skilltimer = Timer(self.skillautocharge,1,1).on()
        self.s1fscharge = 0

    def skillautocharge(self, t):
        self.s1.charge(999999.0*0.08)
        self.s2.charge(999999.0*0.05)
        log('sp','s1autocharge')

    def s1_proc(self, e):
        if self.s1defdown :
            Debuff('s1defdown',0.15,10,1).on()
        self.s1fscharge = 1

    def s2_proc(self, e):
        self.afflics.poison('s2',120,3.00,24)

    def fs_proc(self, e):
        if self.s1fscharge > 0:
            self.s1fscharge -= 1
            self.dmg_make("o_fs_boost",0.21*3)
            self.afflics.poison('fs',self.proc_chance,3.00,24)

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
