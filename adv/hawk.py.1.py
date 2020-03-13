import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import adv.adv_test
from core.advbase import *
from module.x_alt import Fs_alt
from slot.a import *
from slot.d import *

def module():
    return Hawk

class Hawk(Adv):
    a1 = [('k_poison',0.3),('k_stun',0.4)]
    conf = {}
    conf['acl'] = """
        `fs, self.fs_alt.uses > 0 and s1.check()
        `s2, s1.check()
        `s1
        `s3, x=4 or x=5
    """
    conf['slot.d'] = Vayu()
    conf['slot.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['afflict_res.stun'] = 80
    conf['afflict_res.poison'] = 0

    def fs_proc_alt(self, e):
        self.afflics.stun('s2_fs', 160)
        self.afflics.poison('s2_fs', 170, 0.582)
    
    def prerun(self):
        conf_fs_alt = {
            'fs.dmg':4.94,
            'fs.hit':19,
            'fs.sp':2400,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        self.s2stance = 0

    def s1_proc(self, e):
        with Modifier("s1killer", "poison_killer", "hit", 2):
            self.dmg_make('s1',4.74)
            self.hits += 1
        with Modifier("s1killer", "stun_killer", "hit", 3.3):
            self.dmg_make('s1',4.74)
            self.hits += 1

    def s2_proc(self, e):
        if self.s2stance == 0:
            self.fsacharge = 2
            self.fs_alt.on(2)
            self.s2stance = 1
        elif self.s2stance == 1:
            with Modifier("s1killer", "poison_killer", "hit", 0.5):
                self.dmg_make('s2',3.16)
                self.hits += 3
            self.s2stance = 0




if __name__ == '__main__':
    #module().comment = 'boost dmg from stun 3 times'
    conf = {}
    adv.adv_test.test(module(), conf)

