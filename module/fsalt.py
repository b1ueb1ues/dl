from core.advbase import *

class Foo(object):
    pass

class Fs_alt(object):
    def on(self):
        self._fs_alt_status = 1
        self.adv.a_fs   = self.a_fs_alt

    def off(self):
        self._fs_alt_status = 0
        self.adv.a_fs   = self.a_fs_origin

    def act_fs_alt(self, e):
        if self._fs_alt_status :
            log("fs_alt","succ")
            dmg_coef = self.altconf["fs.dmg"]
            self.adv.dmg_make("o_fs_alt", dmg_coef)
            self.adv.fs_proc(e)
            self.adv.think_pin("fs")
            self.adv.charge("fs",self.altconf["fs.sp"])
        else:
            self.adv.l_fs(e)

    def __call__(self):
        doing = self.adv.action.getdoing()
        return self.a_fs_alt(doing.name)

    def __init__(self, adv, altconf):
        self.adv = adv
        self.altconf = altconf
        self.a_fs_alt = Fs_group('fs_alt', altconf, self.act_fs_alt)
        self.a_fs_origin = adv.a_fs
        self._fs_alt_status = 0

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


    
