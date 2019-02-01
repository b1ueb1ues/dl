import adv_test
from adv import *

def module():
    return Kuhai

class Kuhai(Adv):
    comment = 'without s2'
    conf = {
        "mod_a"   : ('crit', 'damage', 0.15),
        "mod_wp" : [ # stellar show for maximum s2 bonus
            ('fs','passive',0.40),
            ('crit','damage',0.13),
            ],
        } 
    def condition(this):
        this.conf["mod_a2"] = ('crit', 'damage', 0.15)
        return 'hp70'

    def init(this):
        this.o_fs = this.fs
        this.fs = this.fs_alt
        this.pfsconf = {
                "fs_dmg":0.83*3,
                "fs_sp": 330,
                "fs_startup":33/60.0,
                "fs_recovery":33/60.0,
                }
        this.a_pfs = Action("fs", this.pfsconf)
        this.a_pfs.e_this = Event('fs_alt')
        this.s2fsbuff = Buff('s2ss',1,10,'ss','ss','self')
        Event('fs_alt').listener(this.l_fs_alt)

    def l_fs_alt(this, e):
        log("fs_alt","succ")
        dmg_p = this.pfsconf["fs_dmg"]
        this.dmg_make("o_fs_alt", dmg_p)
        this.fs_proc(e)
        this.think_pin("fs")
        this.charge("fs",this.pfsconf["fs_sp"])

    def fs_alt(this):
        if this.s2fsbuff.get():
            return this.a_pfs()
        else:
            return this.o_fs()


    def s2_proc(this, e):
        this.s2fsbuff.on() 
    

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

    module().comment = 'use s2'
    # c1+fs_alt has higher dps and sp rate than c2+fs_alt
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=1 and this.s2fsbuff.get()
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0, mass=0)
