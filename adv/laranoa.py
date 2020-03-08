import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Laranoa

class Laranoa(Adv):
    comment = 'doesn\'t count spbuff for teammates'

    a3 = ('s',0.3)
    conf = {}
    #conf['slot.a'] = FB()+The_Prince_of_Dragonyule()
    conf['acl'] = """
        `s1
        `s2,fsc
        `s3,fsc
        `fs, seq=4
        """
    conf['slot.d'] = Siren()
    
    def init(self):
        if self.condition('buff all team'):
            self.s2_proc = self.c_s2_proc

    def prerun(self):
        self.ahits = 0

    
    def c_s2_proc(self, e):
        Teambuff('s2_str',0.10,10).on()
        Selfbuff('s2_sp',0.20,10,'sp','passive').on()

    def s2_proc(self, e):
        Selfbuff('s2_str',0.10,10).on()
        Selfbuff('s2_sp',0.20,10,'sp','passive').on()

    def dmg_proc(self, name, amount):
        if self.hits // 20 > self.ahits:
            self.ahits = self.hits // 20
            Selfbuff('sylvan critdmg',0.10,20,'crit','damage').on()



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


