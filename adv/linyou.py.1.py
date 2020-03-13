import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import adv.adv_test
from core.advbase import *
from module.x_alt import Fs_alt
from slot import *
from slot.a import *
from slot.d import *

def module():
    return Lin_You

class Lin_You(Adv):
    comment = 'c5fs ' 
    a1 = [('cc',0.10,'hp70'),('cc',0.20,'hit25'),('cc',0.20,'hit50')]
    a3 = ('sp',0.08)
    conf = {}
    conf['slot.d'] = Long_Long()
    conf['acl'] = """
        `s2
        `s1
        `s3, fsc or seq=5
        `fs, seq=5
        """

    def d_slots(self):
        if 'bow' in self.ex:
            self.conf.slot.a = KFM()+JotS()
        else:
            self.conf.slot.a = Primal_Crisis()+The_Wyrmclan_Duo()

    def prerun(self):
        conf_fs_alt = {
            'fs.dmg':2.59,
            'fs.hit':6,
            'fs.sp':300,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt))
        self.s2ssbuff = Selfbuff("s2_s1",1, 15, 'ss','ss')
        self.s2spdbuff = Spdbuff("s2_spd",0.2, 15)


    def s1_proc(self, e):
        self.fsacharge = 3
        self.fs_alt.on(3)
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

