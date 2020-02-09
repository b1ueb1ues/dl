from slot import *
from adv import *

class Cerberus(DragonBase):
    ele = 'flame'
    att = 127
    a = [('a', 0.6)]

class Arctos(DragonBase):
    ele = 'flame'
    att = 121
    a = [('a', 0.45), ('cd', 0.55)]

class Prometheus(DragonBase):
    ele = 'flame'
    att = 121
    a = [('a', 0.5)]

class Sakuya(DragonBase):
    ele = 'flame'
    att = 121
    a = [('s', 0.9), ('a', 0.2)]

class Apollo(DragonBase):
    ele = 'flame'
    att = 127
    a = [('k_burn', 0.2), ('a', 0.5)]
    dragonform = {
        'duration': 600 / 60, # 10s dragon time
        'dracolith': 0.40,
        'act': 'c3 s',

        'dshift.startup': 96 / 60, # shift 102 -> 96 + 6
        'dshift.recovery': 6 / 60,
        'dshift.dmg': 2.00,
        'dshift.hit': 1,

        'dx1.dmg': 1.90,
        'dx1.startup': 23 / 60.0, # c1 frames
        'dx1.recovery': 36 / 60.0, # c2 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.09,
        'dx2.startup': 0,
        'dx2.recovery': 35 / 60.0, # c3 frames
        'dx2.hit': 1,

        'dx3.dmg': 2.57,
        'dx3.startup': 0,
        'dx3.recovery': 40 / 60.0, # dodge frames
        'dx3.hit': 1,

        'ds.startup': 110 / 60, # skill frames
        'ds.recovery': 0,
        'ds.hit': 2,
    }
    
    def ds_proc(self):
        from adv import Debuff
        self.adv.dmg_make('o_d_ds',1.80)
        Debuff('ds',0.05,10).on()
        self.adv.afflics.burn('o_d_ds',120,0.311,30,dtype='s')
        self.adv.dmg_make('o_d_ds',4.20)

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