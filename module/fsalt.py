from core.advbase import *

class Foo(object):
    pass

class Fs_alt(object):
    def on(this):
        this._fs_alt_status = 1
        this.adv.a_fs   = this.a_fs_alt

    def off(this):
        this._fs_alt_status = 0
        this.adv.a_fs   = this.a_fs_origin

    def act_fs_alt(this, e):
        if this._fs_alt_status :
            log("fs_alt","succ")
            dmg_coef = this.altconf["fs.dmg"]
            this.adv.dmg_make("o_fs_alt", dmg_coef)
            this.adv.fs_proc(e)
            this.adv.think_pin("fs")
            this.adv.charge("fs",this.altconf["fs.sp"])
        else:
            this.adv.l_fs(e)

    def __call__(this):
        doing = this.adv.action.getdoing()
        return this.a_fs_alt(doing.name)

    def __init__(this, adv, altconf):
        this.adv = adv
        this.altconf = altconf
        this.a_fs_alt = Fs_group('fs_alt', altconf, this.act_fs_alt)
        this.a_fs_origin = adv.a_fs
        this._fs_alt_status = 0

        #adv.l_fs.off()


def fs_alt(adv):
    adv._fs_alt_status = 1
    adv.a_fs   = adv._fs_alt.a_fs 

def fs_back(adv):
    adv._fs_alt_status = 0
    adv.a_fs   = adv._fs_origin.a_fs 

def fs_alt_init(adv, altconf):
    def act_fs_alt(e):
        if adv._fs_alt_status :
            log("fs_alt","succ")
            dmg_coef = altconf["fs.dmg"]
            adv.dmg_make("o_fs_alt", dmg_coef)
            adv.fs_proc(e)
            adv.think_pin("fs")
            adv.charge("fs",altconf["fs.sp"])
        else:
            adv.l_fs(e)
    alt = Foo()
    origin = Foo()

    alt.a_fs = Fs_group('fs_alt',altconf, act_fs_alt)

    origin.a_fs   = adv.a_fs

    adv._fs_alt = alt
    adv._fs_origin = origin
    adv._fs_alt_status = 0

    #adv.l_fs.off()


    
