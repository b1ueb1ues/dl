import adv_test
from adv import *

def module():
    return Kuhai

class Kuhai_alt(Adv):
    adv_name = 'Kuhai'
    conf = {
        "x2fs_startup":18/60.0,
        "x2fs_recovery":33/60.0,
        "x3fs_startup":18/60.0,
        "x3fs_recovery":33/60.0,
        "fs_startup":33/60.0,
        "fs_recovery":33/60.0,
    }
    def __init__(this):
        Adv.__init__(this,{},Timeline())
        #this.setconfig()
        e = Event("fs_alt")
        this.a_x1fs.e_this = e
        this.a_x2fs.e_this = e
        this.a_x3fs.e_this = e
        this.a_x4fs.e_this = e
        this.a_x5fs.e_this = e
        this.a_fs.e_this = e


class Kuhai(Adv):
    comment = 'c2+fs during s2 & stellar show(WP)'
    conf = {
        "mod_a"   : ('crit', 'damage', 0.15),
        } 

    def condition(this):
        this.conf["mod_a2"] = ('crit', 'damage', 0.15)
        this.o_init = this.init
        this.init = this.c_init
        return 'huge hitbox enemy & hp70'

    def condition2(this):
        this.conf["mod_a2"] = ('crit', 'damage', 0.15)
        return 'hp70'
    
    def c_init(this):
        this.o_init()
        this.fsaconf['fs_dmg'] = 0.83*3

    def init(this):
        this.ka = Kuhai_alt()
        this.setconfig()
        this.o_fs = this.fs
        this.fs = this.fs_alt
        this.fsaconf = {
                'fs_dmg':0.83*2,
                'fs_sp' :330,
                }
        this.s2fsbuff = Buff('s2ss',1,10,'ss','ss','self')
        Event('fs_alt').listener(this.l_fs_alt)


    def l_fs_alt(this, e):
        log("fs_alt","succ")
        dmg_p = this.fsaconf["fs_dmg"]
        this.dmg_make("o_fs_alt", dmg_p)
        this.fs_proc(e)
        this.think_pin("fs")
        this.charge("fs",this.fsaconf["fs_sp"])

    def fs_alt(this):
        if this.s2fsbuff.get():
            return this.ka.fs()
        else:
            return this.o_fs()

    def s2_proc(this, e):
        this.s2fsbuff.on() 


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
    conf["mod_wp"] = [ # stellar show for maximum s2 bonus
        ('fs','passive',0.40),
        ('crit','damage',0.13),
        ]
    adv_test.test(module(), conf, verbose=0, mass=0)

    module().comment = 'no s2'
    module().condition = module().condition2
    conf = {}
    conf['acl'] = """
        `s1
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0, mass=0)
