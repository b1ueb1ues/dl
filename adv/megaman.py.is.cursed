import adv_test
from adv import *
from module.fsalt import *
from slot.a import *

def module():
    return Megaman

class Megaman(Adv):

    conf = {}
    conf.slot.a = FoG()+LC()

    def prerun(this):
        this.weapon = 0
        this.ammo = {
                '1':0,
                '2':0,
                }
        this.fsacharge = -1
        this.fsa3conf = Conf()
        this.fsa3conf.fs = Conf(this.conf.fs)
        this.fsa3conf({
                'fs.dmg':0.83*2+0.92,
                'fs.sp' :330,
                "fs.startup":68/60.0,
                "x1fs.startup":77/60.0,
                "x2fs.startup":62/60.0,
                "x3fs.startup":62/60.0,

                "fs.recovery":13/60.0,
                "x1fs.recovery":13/60.0,
                "x2fs.recovery":13/60.0,
                "x3fs.recovery":13/60.0,
                })
        this.fsa1conf = Conf()
        this.fsa1conf.fs = Conf(this.conf.fs)
        this.fsa1conf({
                'fs.dmg':0.83,
                'fs.sp' :330,
                "fs.startup":33/60.0,
                "x1fs.startup":47/60.0,
                "x2fs.startup":32/60.0,
                "x3fs.startup":32/60.0,

                "fs.recovery":43/60.0,
                "x1fs.recovery":43/60.0,
                "x2fs.recovery":43/60.0,
                "x3fs.recovery":43/60.0,
                })
        this.fs_alt3 = Fs_alt(this, this.fsa3conf)
        this.fs_alt1 = Fs_alt(this, this.fsa1conf)
        this.fs_alt = this.fs_alt3
        #fs_alt_init(this, this.fsaconf)

        this.now = core.timeline.now

    def dmg_proc(this, name, amount):
        if name == 'x1':
            this.ammo['1'] += 50
            this.ammo['2'] += 50
        elif name == 'x2':
            this.ammo['1'] += 50
            this.ammo['2'] += 50
        elif name == 'x3':
            this.ammo['1'] += 50
            this.ammo['2'] += 50
        elif name == 'x4':
            this.ammo['1'] += 50
            this.ammo['2'] += 50
        elif name == 'x5':
            this.ammo['1'] += 50
            this.ammo['2'] += 50
        elif name == 'fs':
            this.ammo['1'] += 180
            this.ammo['2'] += 180

    def fs_proc(this, e):
        if this.fsacharge > 0:
            this.fsacharge -= 1
            if this.fsacharge == 0:
                this.fs_alt.off()
                this.fsacharge = -1

    def s1_proc(this, e):
        if this.weapon != 1:
            this.weapon = 1
        else:
            this.weapon = 0
            return 0

    def s2_proc(this, e):
        if this.weapon != 2:
            this.weapon = 2
        else:
            this.weapon = 0
            return 0

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s3, fsc
        `fs, seq=2 and this.gauges['x'] <= 500
        `fs, seq=3
    """

    adv_test.test(module(), conf, verbose=0, mass=0)
