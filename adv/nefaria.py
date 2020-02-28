import adv.adv_test
from core.advbase import *
from module.fsalt import *
from slot.a import *

def module():
    return Nefaria

class Nefaria(Adv):
    a1 = ('k_poison',0.3)
    a3 = ('k_blind',0.4)
    conf = {}
    conf['slot.a'] = MF()+DD()
    conf['acl'] = """
        `s2
        `s1
        `s3, fsc
        `fs, x=4 or s=2
        """
    conf['afflict_res.blind'] = 80
    conf['afflict_res.poison'] = 0

    def prerun(this):
        this.fsacharge = -1
        this.fsaconf = Conf()
        this.fsaconf.fs = Conf(this.conf.fs)
        this.fsaconf( {
                'fs.dmg':19*0.53,
                'fs.sp':2400,
                })
        this.fs_alt = Fs_alt(this, this.fsaconf)
        
        if this.condition('hp100'):
            this.fullhp = 1
        else:
            this.fullhp = 0

    def s1_proc(this, e):
        if this.afflics.poison.get() != 0:
            with Modifier("s1killer", "poison_killer", "hit", 0.74):
                this.afflics.poison('s1', 120+this.fullhp*60, 0.582)
                this.dmg_make('s1',8*1.06)
        elif this.afflics.blind.get() != 0:
            with Modifier("s1killer", "blind_killer", "hit", 0.74):
                this.afflics.poison('s1', 120+this.fullhp*60, 0.582)
                this.dmg_make('s1',8*1.06)
        else:
            this.afflics.poison('s1', 120+this.fullhp*60, 0.582)
            this.dmg_make('s1',8*1.06)

    def s2_proc(this, e):
        this.fsacharge = 1
        this.fs_alt.on()

    def fs_proc(this, e):
        if this.fsacharge > 0:
            this.fsacharge -= 1
            this.afflics.blind('s2_fs', 100+this.fullhp*60)
            if this.fsacharge == 0:
                this.fs_alt.off()
                this.fsacharge = -1


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
