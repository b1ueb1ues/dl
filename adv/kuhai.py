import adv_test
from adv import *
from module.fsalt import *
import slot

def module():
    return Kuhai


class Kuhai(Adv):
    comment = 'c2+fs during s2 & stellar show + RR'
    a1 = ('cd',0.15)
    a3 = ('cd',0.15, 'hp70')

    def pre(this):
        if this.condition('huge hitbox eneny'):
            this.o_init = this.init
            this.init = this.c_init
        else:
            this.missc1 = this.c_missc1
            this.backc1 = this.c_backc1

    def pre2(this):
        pass
    
    def c_init(this):
        this.o_init()
        this.fsaconf['fs.dmg'] = 0.83*3

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


    def init(this):
        this.fsaconf = Conf()
        this.fsaconf.fs = Conf(this.conf.fs)
        this.fsaconf({
                'fs.dmg':0.83*2,
                'fs.sp' :330,
                "fs.startup":33/60.0,
                "fs.recovery":33/60.0,
                "x2fs.startup":18/60.0,
                "x2fs.recovery":33/60.0,
                "x3fs.startup":18/60.0,
                "x3fs.recovery":33/60.0,
                })
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
    # c1+fs_alt has higher dps and sp rate than c2+fs_alt with or without stellar show  (x)
    # c2+fs_alt fs can init quicker than c1+fs_alt 
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=2 and this.s2fsbuff.get()
        `fs, seq=3
        """
    conf['slots.a'] = slot.a.Stellar_Show() + slot.a.RR()
    adv_test.test(module(), conf, verbose=0, mass=0)

    exit()

    module().comment = 'no s2 & RR+LC'
    module().pre = module().pre2
    conf = {}
    conf['mod_wp'] = [('s','passive',0.25),
                  ('crit','chance',0.06,'hp70')]
    conf['mod_wp2'] = [('crit','damage',0.13),
                  ('crit','chance',0.08,'hp70')]
    conf['str_wp2'] = 64
    #conf['mod_wp2'] = [('s','passive',0.10),
    #              ('fs','passive',0.30)]
    conf['acl'] = """
        `s1
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0, mass=0)
