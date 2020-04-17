from core.advbase import *
from module.x_alt import Fs_alt
import slot
from slot.a import *
from slot.d import *

def module():
    return Ku_Hai

class Ku_Hai(Adv):
    comment = 'c2+fs during s2'
    a1 = ('cd',0.15)
    a3 = ('cd',0.15, 'hp70')
    conf = {}
    # c1+fs_alt has higher dps and sp rate than c2+fs_alt with or without stellar show  (x)
    # c2+fs_alt fs can init quicker than c1+fs_alt
    conf['slots.a'] = The_Lurker_in_the_Woods()+The_Shining_Overlord()
    conf['slots.d'] = AC011_Garland()
    conf['acl'] = '''
        `dragon.act("c3 s c1 end")
        `s1, fsc
        `s2
        `s3, fsc
        `fs, seq=2 and self.fs_alt.get()
        `fs, seq=3
        '''
    coab = ['Blade','Dragonyule_Xainfried','Akasha']

    def init(self):
        if self.condition('huge hitbox eneny'):
            self.o_prerun = self.prerun
            self.prerun = self.c_prerun
        else:
            self.missc1 = self.c_missc1
            self.backc1 = self.c_backc1

    def pre2(self):
        pass

    def c_prerun(self):
        self.o_prerun()
        self.fshit = 3
        self.fs_alt.conf_alt['fs.dmg'] = 0

    def missc1(self):
        pass

    def backc1(self):
        pass

    def c_missc1(self):
        self.x1dmgb = self.conf['x1.dmg']
        self.x1spb = self.conf['x1.sp']
        self.conf['x1.dmg'] = 0
        self.conf['x1.sp'] = 0

    def c_backc1(self):
        self.conf['x1.dmg'] = self.x1dmgb
        self.conf['x1.sp'] = self.x1spb

    def fs_proc_alt(self, e):
        self.dmg_make('o_fs_alt_hit1',0.83)
        if self.fshit >= 2:
            self.dmg_make('o_fs_alt_hit2',0.83)
        if self.fshit >= 3:
            self.dmg_make('o_fs_alt_hit3',0.83)

    def prerun(self):
        self.fshit = 2
        self.alttimer = Timer(self.altend)
        conf_fs_alt = {
            'fs.dmg':0,
            'fs.sp' :330,
            'fs.charge': 2/60.0, # needs confirm
            'fs.startup':31/60.0,
            'fs.recovery':33/60.0,
            'x2fs.startup':16/60.0,
            'x2fs.recovery':33/60.0,
            'x3fs.startup':16/60.0,
            'x3fs.recovery':33/60.0,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)

    def altend(self,t):
        self.fs_alt.off()
        self.backc1()

    def s2_proc(self, e):
        self.fs_alt.on(-1)
        self.alttimer.on(10)
        self.missc1()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)