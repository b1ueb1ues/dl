import adv.adv_test
from core.advbase import *
from slot import *
from slot.a import *

def module():
    return Lin_You

class Lin_You(Adv):
    comment = '2in1 ' 
    a1 = ('cc',0.10,'hp70')
    a3 = ('sp',0.08)
    conf = {}
    conf['acl'] = """
        `s2, s1.charged>=s1.sp-440 
        `s1
        `s2, seq=4
        `s3, seq=5
        """

    def d_slots(self):
        if 'bow' in self.ex:
            self.conf.slot.a = KFM()+JotS()
        else:
            self.conf.slot.a = KFM()+CE()

    def prerun(self):
        self.s2ssbuff = Selfbuff("s2_s1",1, 10, 'ss','ss')
        self.s2spdbuff = Spdbuff("s2_spd",0.2, 10)


    def s1_proc(self, e):
        if self.s2ssbuff.get():
            self.dmg_make('o_s1_powerup',1.86*3)
            self.s2ssbuff.buff_end_timer.timing += 2.4
            self.s2spdbuff.buff_end_timer.timing += 2.4


    def s2_proc(self, e):
        self.s2ssbuff.on()
        self.s2spdbuff.on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

