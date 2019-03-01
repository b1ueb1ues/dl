from core.advbase import *

class Foo(object):
    pass

def fs_alt(adv):
    adv._fs_alt_status = 1
    adv.a_fs   = adv._fs_alt.a_fs 
    adv.a_x1fs = adv._fs_alt.a_x1fs
    adv.a_x2fs = adv._fs_alt.a_x2fs
    adv.a_x3fs = adv._fs_alt.a_x3fs
    adv.a_x4fs = adv._fs_alt.a_x4fs
    adv.a_x5fs = adv._fs_alt.a_x5fs

def fs_back(adv):
    adv._fs_alt_status = 0
    adv.a_fs   = adv._fs_origin.a_fs 
    adv.a_x1fs = adv._fs_origin.a_x1fs
    adv.a_x2fs = adv._fs_origin.a_x2fs
    adv.a_x3fs = adv._fs_origin.a_x3fs
    adv.a_x4fs = adv._fs_origin.a_x4fs
    adv.a_x5fs = adv._fs_origin.a_x5fs

def fs_alt_init(adv, altconf):
    this = Foo()
    origin = Foo()
    fsconf = {}
    xnfsconf = {}
    xn = {}
    for i in altconf:
        if i[:3] == 'fs_':
            fsconf[i] = altconf[i]
        if i[2:5] == 'fs_':
            xnfsconf[i] = altconf[i]
            xn[i[:4]] = 1
    this.a_fs = Action('fs',fsconf)

    for i in ['x1fs','x2fs','x3fs','x4fs','x5fs']:
        tmpconf = {}
        for j in xnfsconf:
            if j[:4] == i:
                tmpconf[j[2:]] = xnfsconf[j]
        if tmpconf == {}:
            setattr(this, 'a_'+i,  this.a_fs )
        else:
            for j in fsconf:
                if j not in tmpconf:
                    tmpconf[j] = fsconf[j]
            setattr(this, 'a_'+i,  Action('fs' ,tmpconf) )

    this.a_fs.cancel_by = ['dodge','s1','fsf','s2','s3']
    this.a_x1fs.cancel_by = ['dodge','s1','s2','s3']
    this.a_x2fs.cancel_by = ['dodge','s1','s2','s3']
    this.a_x3fs.cancel_by = ['dodge','s1','s2','s3']
    this.a_x4fs.cancel_by = ['dodge','s1','s2','s3']
    this.a_x5fs.cancel_by = ['dodge','s1','s2','s3']

    this.a_fs.interrupt_by = ['s1','s2','s3']
    this.a_x1fs.interrupt_by = ['s1','s2','s3']
    this.a_x2fs.interrupt_by = ['s1','s2','s3']
    this.a_x3fs.interrupt_by = ['s1','s2','s3']
    this.a_x4fs.interrupt_by = ['s1','s2','s3']
    this.a_x5fs.interrupt_by = ['s1','s2','s3']

    origin.a_fs   = adv.a_fs
    origin.a_x1fs = adv.a_x1fs
    origin.a_x2fs = adv.a_x2fs
    origin.a_x3fs = adv.a_x3fs
    origin.a_x4fs = adv.a_x4fs
    origin.a_x5fs = adv.a_x5fs

    adv._fs_alt = this
    adv._fs_origin = origin
    adv._fs_alt_status = 0

    adv.l_fs.off()

    def l_fs_alt(e):
        if adv._fs_alt_status :
            log("fs_alt","succ")
            dmg_p = altconf["fs_dmg"]
            adv.dmg_make("o_fs_alt", dmg_p)
            adv.fs_proc(e)
            adv.think_pin("fs")
            adv.charge("fs",altconf["fs_sp"])
        else:
            adv.l_fs(e)

    adv.l_fs_alt = Listener(['fs','x1fs','x2fs','x3fs','x4fs','x5fs'], l_fs_alt)
    
