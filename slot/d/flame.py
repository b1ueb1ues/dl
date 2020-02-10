from slot import *
from adv import *

class Cerberus(DragonBase):
    ele = 'flame'
    att = 127
    a = [('a', 0.6)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.00,
        'dx1.startup': 12 / 60.0, # c1 frames
        'dx1.recovery': 26 / 60.0, # c2 frames
        'dx1.hit': 1,

        'dx2.dmg': 1.40,
        'dx2.recovery': (41+15) / 60.0, # c3 frames
        'dx2.hit': 1,

        'dx3.dmg': 1.40*2,
        'dx3.recovery': 38 / 60.0, # recovery
        'dx3.hit': 2,

        'ds.recovery': 270 / 60, # skill frames
        'ds.hit': 7,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from adv import Debuff
        self.ds_buff = Debuff('ds',0.05,10)

    def ds_proc(self):
        dmg = self.adv.dmg_make('d_ds',1.10,'s')
        self.ds_buff.on()
        self.adv.afflics.burn('ds',120,0.97,12,dtype='s')
        return dmg + self.adv.dmg_make('d_ds',1.10*6,'s')

class Arctos(DragonBase):
    ele = 'flame'
    att = 121
    a = [('a', 0.45), ('cd', 0.55)]
    dragonform = {
        'act': 's c3',

        'dx1.dmg': 2.10,
        'dx1.startup': 19 / 60.0, # c1 frames
        'dx1.recovery': 39 / 60.0, # c2 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.31,
        'dx2.recovery': (60+27) / 60.0, # c3 frames
        'dx2.hit': 1,

        'dx3.dmg': 4.20*2,
        'dx3.recovery': 40 / 60.0, # dodge frames, real recovery 56
        'dx3.hit': 2,

        'ds.dmg': 10,
        'ds.recovery': 168 / 60, # skill frames
        'ds.hit': 2,
    }

class Prometheus(DragonBase):
    ele = 'flame'
    att = 121
    a = [('a', 0.5)]
    dragonform = {
        'act': 's c3',

        'dx1.dmg': 1.60,
        'dx1.startup': 14 / 60.0, # c1 frames
        'dx1.recovery': 36 / 60.0, # c2 frames
        'dx1.hit': 1,

        'dx2.dmg': 1.76,
        'dx2.recovery': 36 / 60.0, # c3 frames
        'dx2.hit': 1,

        'dx3.dmg': 2.24,
        'dx3.recovery': 39 / 60.0, # dodge frames, real recovery 56
        'dx3.hit': 2,

        'ds.dmg': 5.60,
        'ds.recovery': 126 / 60, # skill frames
        'ds.hit': 2,
    }

class Sakuya(DragonBase):
    ele = 'flame'
    att = 121
    a = [('s', 0.9), ('a', 0.2)]
    dragonform = {
        'act': 'c3 s end',

        'dx1.dmg': 2.08,
        'dx1.startup': 25 / 60.0, # c1 frames
        'dx1.recovery': 40 / 60.0, # c2 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.29,
        'dx2.recovery': 48 / 60.0, # c3 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.99,
        'dx3.recovery': 40 / 60.0, # dodge frames, real recovery 69
        'dx3.hit': 1,

        'ds.recovery': 167 / 60, # skill frames
        'ds.hit': -1,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from adv import SingleActionBuff
        self.ds_buff = SingleActionBuff('d_sd_buff',0.40,1,'s','buff')

    def ds_proc(self):
        self.ds_buff.on(1)
        return self.adv.dmg_make('d_ds',6.60,'s')

class Apollo(DragonBase):
    ele = 'flame'
    att = 127
    a = [('k_burn', 0.2), ('a', 0.5)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 1.90,
        'dx1.startup': 23 / 60.0, # c1 frames
        'dx1.recovery': 36 / 60.0, # c2 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.09,
        'dx2.recovery': 35 / 60.0, # c3 frames
        'dx2.hit': 1,

        'dx3.dmg': 2.57,
        'dx3.recovery': 40 / 60.0, # dodge frames, real recovery 41
        'dx3.hit': 1,

        'ds.recovery': 110 / 60, # skill frames
        'ds.hit': 2,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from adv import Debuff
        self.ds_buff = Debuff('ds',0.05,10)

    def ds_proc(self):
        dmg = self.adv.dmg_make('d_ds',1.80,'s')
        self.ds_buff.on()
        self.adv.afflics.burn('ds',120,0.311,30,dtype='s')
        return dmg + self.adv.dmg_make('d_ds',4.20,'s')

class Kagutsuchi(DragonBase):
    ele = 'flame'
    att = 127
    a = [('primed_att', 0.15), ('a', 0.45)]

class Dreadking_Rathalos(DragonBase):
    ele = 'flame'
    att = 127
    a = [('a', 0.55), ('fs', 0.60), ('sp',0.30,'fs')]

class Unreleased_FlameSkillHaste(DragonBase):
    ele = 'flame'
    att = 120
    a = [('sp', 0.35)]

class Unreleased_Flame80Str(DragonBase):
    ele = 'flame'
    att = 127
    a = [('a', 0.8, 'some wacky condition')]