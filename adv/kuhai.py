if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from module.fsalt import *
import slot
from slot.d import *

def module():
    return Kuhai


class Kuhai(Adv):
    comment = 'c2+fs during s2'
    a1 = ('cd',0.15)
    a3 = ('cd',0.15, 'hp70')
    conf = {}
    # c1+fs_alt has higher dps and sp rate than c2+fs_alt with or without stellar show  (x)
    # c2+fs_alt fs can init quicker than c1+fs_alt 
    conf['acl'] = """
        `s1, fsc
        `s2
        `s3, fsc
        `fs, seq=2 and this.s2fsbuff.get()
        `fs, seq=3
        """
    conf['slots.a'] = slot.a.Stellar_Show() + slot.a.RR()
    conf['slot.d'] = Hastur()

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
        this.fsaconf['fs.dmg'] = 0

    def fs_proc(this, e):
        if e.name != 'fs_alt' :
            return
        this.dmg_make('o_fs_alt_hit1',0.83)
        if this.fshit >= 2:
            this.dmg_make('o_fs_alt_hit2',0.83)
        if this.fshit >= 3:
            this.dmg_make('o_fs_alt_hit3',0.83)


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


    def prerun(this):
        this.fsaconf = Conf()
        this.fsaconf.fs = Conf(this.conf.fs)
        this.fsaconf({
                'fs.dmg':0,
                'fs.sp' :330,
                "fs.startup":33/60.0,
                "fs.recovery":33/60.0,
                "x2fs.startup":18/60.0,
                "x2fs.recovery":33/60.0,
                "x3fs.startup":18/60.0,
                "x3fs.recovery":33/60.0,
                })
        this.fshit = 2
        this.s2fsbuff = Selfbuff('s2ss',1,10,'ss','ss')
        this.alttimer = Timer(this.altend)
        fs_alt_init(this, this.fsaconf)

    def altend(this,t):
        fs_back(this)
        this.backc1()

    def s2_proc(this, e):
        this.s2fsbuff.on() 
        fs_alt(this)
        this.missc1()
        this.alttimer.on(10)


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

