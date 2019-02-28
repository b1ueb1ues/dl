import adv_test
from adv import *

def module():
    return Albert



class Albert(Adv):
    conf = {
            'mod_a':('fs','passive',0.5),
            'mod_wp':('s','passive',0.35),
            }

    def init(this):
        this.fsa_conf = {
                'fsa_dmg':1.02,
                'fsa_dmg':330,
                #'fsa_startup':18,
                #'fsa_recovery':18,
                }
        this.s2timer = Timer(this.s2autocharge,1,1).on()
        this.paralyze_count=3
        this.s2buff = Buff("s2_shapshift",1, 20,'ss','ss','self')
        this.a2buff = Buff('a2_str_passive',0.2,20,'att','passive','self')
        Event('fs_alt').listener(this.l_fs_alt)

    def fs_alt(this):
        this.a_fs.reinit('fs_alt')
        this.a_x1fs.reinit('fs_alt')
        this.a_x2fs.reinit('fs_alt')
        this.a_x3fs.reinit('fs_alt')
        this.a_x4fs.reinit('fs_alt')
        this.a_x5fs.reinit('fs_alt')

    def fs_back(this):
        this.a_fs.reinit('fs')
        this.a_x1fs.reinit('fs')
        this.a_x2fs.reinit('fs')
        this.a_x3fs.reinit('fs')
        this.a_x4fs.reinit('fs')
        this.a_x5fs.reinit('fs')

    def l_fs_alt(this, e):
        log("fs_alt","succ")
        dmg_p = this.fsaconf["fsa_dmg"]
        this.dmg_make("o_fs_alt", dmg_p)
        this.fs_proc(e)
        this.think_pin("fs")
        this.charge("fs",this.fsaconf["fsa_sp"])


    def s2autocharge(this, t):
        if not this.a2buff.get():
            this.s2.charge(160000.0/40)
            log('sp','s2autocharge')

            
    def condition(this):
        this.conf['acl'] = """
            `s2, s1.charged>=s1.sp
            `s1
            `fs, seq=2
            """
        return '3s1 in one s2'


    def s1_proc(this, e):
        if this.s2buff.get():
            this.dmg_make("o_s1_s2boost",12.38-0.825+0.83*5)


    def fs_proc(this, e):
        if this.paralyze_count > 0:
            if this.s2buff.get():
                this.paralyze_count -= 1
                this.dmg_make("o_s1_paralyze",0.803*3)

    def s2_proc(this, e):
        this.s2timer.on()
        this.s2buff.on()
        this.a2buff.on()
        #this.fs_alt()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2
        `s1
        `fs, seq=2
        """
    adv_test.test(module(), conf,verbose=0, mass=0)

