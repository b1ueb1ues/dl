from core.advbase import *

class Foo(object):
    pass

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


    
