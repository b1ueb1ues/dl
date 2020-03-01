import adv.adv_test
from core.advbase import *
from module.x_alt import Fs_alt
import slot
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
    conf['acl'] = '''
        `s1, fsc
        `s2
        `s3, fsc
        `fs, seq=2 and this.fs_alt.get()
        `fs, seq=3
        '''
    conf['slots.a'] = slot.a.The_Lurker_in_the_Woods() + slot.a.RR()
    conf['slot.d'] = Zephyr()

    def init(this):
        if this.condition('huge hitbox eneny'):
            this.o_prerun = this.prerun
            this.prerun = this.c_prerun
        else:
            this.missc1 = this.c_missc1
            this.backc1 = this.c_backc1

    def pre2(this):
        pass

    def c_prerun(this):
        this.o_prerun()
        this.fshit = 3
        this.fs_alt.conf_alt['fs.dmg'] = 0

    def missc1(this):
        pass

    def backc1(this):
        pass

    def c_missc1(this):
        this.x1dmgb = this.conf['x1.dmg']
        this.x1spb = this.conf['x1.sp']
        this.conf['x1.dmg'] = 0
        this.conf['x1.sp'] = 0

    def c_backc1(this):
        this.conf['x1.dmg'] = this.x1dmgb
        this.conf['x1.sp'] = this.x1spb

    def fs_proc_alt(this, e):
        this.dmg_make('o_fs_alt_hit1',0.83)
        if this.fshit >= 2:
            this.dmg_make('o_fs_alt_hit2',0.83)
        if this.fshit >= 3:
            this.dmg_make('o_fs_alt_hit3',0.83)

    def prerun(this):
        this.fshit = 2
        this.alttimer = Timer(this.altend)
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
        this.fs_alt = Fs_alt(this, Conf(conf_fs_alt), this.fs_proc_alt)

    def altend(this,t):
        this.fs_alt.off()
        this.backc1()

    def s2_proc(this, e):
        this.fs_alt.on(-1)
        this.alttimer.on(10)
        this.missc1()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

