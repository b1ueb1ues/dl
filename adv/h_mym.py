import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return H_Mym

class H_Mym(Adv):
    conf = {}
    conf['slots.a'] = KFM()+Jewels_of_the_Sun()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, cancel
        `fs, x=5
    """
    conf['dragonform'] = {
        'act': 'c3 s',

        'dx1.dmg': 2.20,
        'dx1.startup': 15 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 3.30,
        'dx2.startup': 44 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.74*2,
        'dx3.startup': (38+24) / 60.0, # c3 frames
        'dx3.recovery': 54 / 60.0, # recovery
        'dx3.hit': 2,

        'ds.dmg': 12.32,
        'ds.recovery': 178 / 60, # skill frames
        'ds.hit': 8,

        'dodge.startup': 41 / 60.0, # dodge frames
    }
    def ds_proc(this):
        return this.dmg_make('d_ds',this.dragonform.conf.ds.dmg,'s')

    def init(this):
        del this.slots.c.ex['axe']
        this.slots.c.ex['axe2'] = ('ex', 'axe2')

    def prerun(this):
        if this.condition('s1 defdown for 10s'):
            this.s1defdown = 1
        else:
            this.s1defdown = 0
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc

        this.s2_da = Selfbuff('a3_dreamboost',0.20,15,'da','buff')

        this.a1_spd = Spdbuff('a1',0.15,-1,wide='self')
        Event('dragon').listener(this.a1_on)
        Event('idle').listener(this.a1_off)

    def a1_on(this, e):
        if not this.a1_spd.get():
            this.a1_spd.on()

    def a1_off(this, e):
        if this.a1_spd.get():
            this.a1_spd.off()

    def s1_proc(this, e):
        if this.s1defdown :
            Debuff('s1defdown',0.15,10,1).on()
    
    def c_s2_proc(this, e):
        Teambuff('s2',0.20,15).on()
        Selfbuff('s2_dreamboost',0.05,15,'crit','rate').on()
        this.s2_da.on()

    def s2_proc(this, e):
        Selfbuff('s2',0.20,15).on()
        Selfbuff('s2_dreamboost',0.05,15,'crit','rate').on()
        this.s2_da.on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0, mass=0)
