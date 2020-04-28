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
        `s3, not self.s3_buff
        `s1, fsc
        `s2
        `fs, seq=2 and self.fs_alt.get()
        `fs, seq=3
        '''
    coab = ['Blade','Dragonyule_Xainfried','Akasha']

    def prerun(self):
        self.fshit = 2
        self.alttimer = Timer(self.altend)
        conf_fs_alt = {
            'fs.dmg':0.83*2,
            'fs.sp' :330,
            'fs.charge': 2/60.0, # needs confirm
            'fs.startup':31/60.0,
            'fs.recovery':33/60.0,
            'fs.hit': 2,
            'x2fs.startup':16/60.0,
            'x2fs.recovery':33/60.0,
            'x3fs.startup':16/60.0,
            'x3fs.recovery':33/60.0,
        }
        if self.condition('big hitbox'):
            conf_fs_alt['fs.dmg'] += 0.83
            conf_fs_alt['fs.hit'] += 1
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt))

    def altend(self,t):
        self.fs_alt.off()

    def s2_proc(self, e):
        self.fs_alt.on(-1)
        self.alttimer.on(10)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)