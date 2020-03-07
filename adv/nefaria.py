import adv.adv_test
from core.advbase import *
from module.x_alt import Fs_alt
from slot.a import *
from slot.d import *

def module():
    return Nefaria

class Nefaria(Adv):
    comment = 's2 fs(precharge) s1 s1'
    a1 = ('k_poison',0.3)
    a3 = ('k_blind',0.4)
    conf = {}
    conf['slot.d'] = Shinobi()
    conf['slot.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['acl'] = """
        `fs, this.fs_alt.uses > 0 and s1.check()
        `s2, s1.check()
        `s1
        `s3, x=4 or x=5
        """
    # conf['acl'] = """
    #     `fs, this.fs_alt.uses > 0 and x=4
    #     `s1, fsc or x=1 or not this.s3_buff
    #     `s2
    #     `s3, not this.s3_buff
    #     """

    conf['afflict_res.blind'] = 80
    conf['afflict_res.poison'] = 0

    def fs_proc_alt(this, e):
        this.afflics.blind('s2_fs', 110+this.fullhp*60)
    
    def prerun(this):
        conf_fs_alt = {
            'fs.dmg':8.09,
            'fs.hit':19,
            'fs.sp':2400,
        }
        this.fs_alt = Fs_alt(this, Conf(conf_fs_alt), this.fs_proc_alt)
        
        if this.condition('hp100'):
            this.fullhp = 1
        else:
            this.fullhp = 0

    def s1_proc(this, e):
        with KillerModifier('s1killer', 'hit', 0.74, ['blind', 'poison']):
            this.dmg_make('s1',1.06)
            this.hits += 1
            this.afflics.poison('s1', 70+this.fullhp*60, 0.582)
            this.dmg_make('s1',7*1.06)
            this.hits += 7

    def s2_proc(this, e):
        this.fsacharge = 1
        this.fs_alt.on(1)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)