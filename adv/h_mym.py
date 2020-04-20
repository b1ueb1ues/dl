from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Halloween_Mym

class Halloween_Mym(Adv):
    conf = {}
    conf['slots.a'] = Kung_Fu_Masters()+Jewels_of_the_Sun()
    conf['slots.d'] = Dreadking_Rathalos()
    conf['slots.burn.d'] = Apollo()
    conf['acl'] = """
        `dragon, s=2
        `s3, not self.s3_buff
        `s1, fsc
        `s2, cancel
        `fs, x=5
    """
    coab = ['Blade', 'Yuya', 'Serena']

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
    def ds_proc(self):
        return self.dmg_make('ds',self.dragonform.conf.ds.dmg,'s')

    def prerun(self):
        if self.condition('s1 defdown for 10s'):
            self.s1defdown = 1
        else:
            self.s1defdown = 0
        if self.condition('buff all team'):
            self.s2_proc = self.c_s2_proc

        self.s2_da = Selfbuff('a3_dreamboost',0.20,15,'da','buff')

        self.a1_spd = Spdbuff('a1',0.15,-1,wide='self')
        Event('dragon').listener(self.a1_on)
        Event('idle').listener(self.a1_off)

    def a1_on(self, e):
        if not self.a1_spd.get():
            self.a1_spd.on()

    def a1_off(self, e):
        if self.a1_spd.get():
            self.a1_spd.off()

    def s1_proc(self, e):
        if self.s1defdown :
            Debuff('s1defdown',0.15,10,1).on()
    
    def c_s2_proc(self, e):
        Teambuff('s2',0.20,15).on()
        Selfbuff('s2_dreamboost',0.05,15,'crit','rate').on()
        self.s2_da.on()

    def s2_proc(self, e):
        Selfbuff('s2',0.20,15).on()
        Selfbuff('s2_dreamboost',0.05,15,'crit','rate').on()
        self.s2_da.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)