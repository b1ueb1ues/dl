import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *
from module.x_alt import Fs_alt

def module():
    return Lin_You

class Lin_You(Adv):
    comment = '2in1 ' 
    a1 = [('cc',0.10,'hp70'), ('cc',0.20,'hit25'), ('cc',0.20,'hit50')]
    a3 = ('sp',0.08)
    conf = {}
    conf['slot.d'] = Long_Long()
    conf['acl'] = """
        `s2, s1.charged>=s1.sp-440 
        `s1
        `s2, seq=4
        `s3, seq=5
        """

    def prerun(self):
        conf_fs_alt = {REPLACE}
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), fs_proc=REPLACE?)
        self.s2_buff = Spdbuff('s2_spd',0.20, 15)

    def s1_proc(self, e):
        if self.s2_buff.get():
            self.dmg_make('o_s1_powerup', REPLACE*3)
            self.s2_buff.buff_end_timer.add(2.4)
            self.hits += 3
        self.fs_alt.on(3)

    def s2_proc(self, e):
        self.s2_buff.on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

