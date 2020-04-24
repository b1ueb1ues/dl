from slot import *
from core.advbase import *

class Agni(DragonBase):
    ele = 'flame'
    att = 127
    a = [('a', 0.6)]
    dragonform = {
        'act': 'c2 c2 c2 c2 c2 s c2',

        'dx1.dmg': 2.80,
        'dx1.startup': 36 / 60.0, # c1 frames
        'dx1.hit': 2,

        'dx2.dmg': 3.08,
        'dx2.startup': 34 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.92,
        'dx3.startup': 79 / 60.0, # c3 frames
        'dx3.recovery': 80 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.dmg': 9.80,
        'ds.recovery': 265 / 60, # skill frames
        'ds.hit': -2,

        'dodge.startup': 39 / 60, # dodge frames
    }

class Cerberus(DragonBase):
    ele = 'flame'
    att = 127
    a = [('a', 0.6)]
    dragonform = {
        'act': 'c3 s', # "c3 c2 s c2 c2 c2 c2 c2 c2"

        'dx1.dmg': 2.00,
        'dx1.startup': 12 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 1.40,
        'dx2.startup': 26 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 1.40*2,
        'dx3.startup': (41+15) / 60.0, # c3 frames
        'dx3.recovery': 38 / 60.0, # recovery
        'dx3.hit': 2,

        'ds.recovery': 270 / 60, # skill frames
        'ds.hit': 7,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from core.advbase import Debuff
        self.ds_buff = Debuff('ds',0.05,10)

    def ds_proc(self):
        dmg = self.adv.dmg_make('ds',1.10,'s')
        self.ds_buff.on()
        self.adv.afflics.burn('ds',120,0.97,12,dtype='s')
        return dmg + self.adv.dmg_make('ds',1.10*6,'s')

class Arctos(DragonBase):
    ele = 'flame'
    att = 121
    a = [('a', 0.45), ('cd', 0.55)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.10,
        'dx1.startup': 19 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.31,
        'dx2.startup': 39 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 4.20*2,
        'dx3.startup': (60+27) / 60.0, # c3 frames
        'dx3.recovery': 56 / 60.0, # recovery
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
        'act': 'c3 s',

        'dx1.dmg': 1.60,
        'dx1.startup': 14 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 1.76,
        'dx2.startup': 36 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 2.24,
        'dx3.startup': 36 / 60.0, # c3 frames
        'dx3.recovery': 56 / 60.0, # recovery
        'dx3.hit': 2,

        'ds.dmg': 5.60,
        'ds.recovery': 126 / 60, # skill frames
        'ds.hit': 2,

        'dodge.startup': 39 / 60, # dodge frames
    }

class Konohana_Sakuya(DragonBase):
    ele = 'flame'
    att = 121
    a = [('s', 0.9), ('a', 0.2)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.08,
        'dx1.startup': 25 / 60.0, # c1 frames
        'dx2.startup': 40 / 60.0, # c2 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.29,
        'dx3.startup': 48 / 60.0, # c3 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.99,
        'dx3.recovery': 69 / 60.0, # recovery
        'dx3.hit': 3,

        'ds.recovery': 167 / 60, # skill frames
        'ds.hit': -1,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from core.advbase import SingleActionBuff
        self.ds_buff = SingleActionBuff('d_sd_buff',0.40,1,'s','buff')

    def ds_proc(self):
        dmg = self.adv.dmg_make('ds',6.60,'s')
        self.ds_buff.on(1)
        return dmg
Sakuya = Konohana_Sakuya

class Apollo(DragonBase):
    ele = 'flame'
    att = 127
    a = [('k_burn', 0.2), ('a', 0.5)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 1.90,
        'dx1.startup': 23 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.09,
        'dx2.startup': 36 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 2.57,
        'dx3.startup': 35 / 60.0, # c3 frames
        'dx3.recovery': 41 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.recovery': 110 / 60, # skill frames
        'ds.hit': 2,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from core.advbase import Debuff
        self.ds_buff = Debuff('ds',0.05,10)

    def ds_proc(self):
        dmg = self.adv.dmg_make('ds',1.80,'s')
        self.ds_buff.on()
        self.adv.afflics.burn('ds',120,0.311,30,dtype='s')
        return dmg + self.adv.dmg_make('ds',4.20,'s')

class Kagutsuchi(DragonBase):
    ele = 'flame'
    att = 127
    a = [('primed_att', 0.15), ('a', 0.45)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.00,
        'dx1.startup': 28 / 60.0, # c1 frames
        'dx2.startup': 48 / 60.0, # c2 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.40,
        'dx3.startup': 63 / 60.0, # c3 frames
        'dx2.hit': 1,

        'dx3.dmg': 5.80,
        'dx3.recovery': 64 / 60.0, # recovery
        'dx3.hit': 2,

        'ds.recovery': 141 / 60, # skill frames
        'ds.hit': 2,
    }

    def ds_proc(self):
        dmg = self.adv.dmg_make('ds',2.20,'s')
        self.adv.afflics.burn('ds',120,0.97,12,dtype='s')
        return dmg + self.adv.dmg_make('ds',4.40,'s')


class Dreadking_Rathalos(DragonBase):
    ele = 'flame'
    att = 127
    a = [('a', 0.55), ('fs', 0.60), ('sp',0.30,'fs')]
    dragonform = {
        'act': 'c1 c1 c3 s',

        'dx1.dmg': 2.20,
        'dx1.startup': 6 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.42,
        'dx2.startup': 41 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 1.44+3.40,
        'dx3.startup': 57 / 60.0, # c3 frames
        'dx3.recovery': 93 / 60.0, # recovery
        'dx3.hit': 2,

        'ds.recovery': 161 / 60, # skill frames
        'ds.hit': 2,

        'dodge.startup': 41 / 60, # dodge frames
    }

    def ds_proc(self):
        dmg = self.adv.dmg_make('ds',1.00,'s')
        self.adv.afflics.burn('ds',120,0.97,12,dtype='s')
        return dmg + self.adv.dmg_make('ds',4.00,'s')

class Gala_Mars(DragonBase):
    ele = 'flame'
    att = 127
    a = [('a', 0.7), ('a', 0.2, 'hp50')]
    dragonform = {
        'skill_use': 2,
        'act': 'c1 s c3 c3 s',

        'dx1.dmg': 2.70,
        'dx1.startup': 15 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.97,
        'dx2.startup': 60 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 4.86,
        'dx3.startup': 81 / 60.0, # c3 frames
        'dx3.recovery': 35 / 60.0, # recovery
        'dx3.hit': 3,

        'ds.recovery': 140 / 60, # skill frames
        'ds.hit': 3,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from core.advbase import Event
        Event('dragon_end').listener(self.shift_end_prep)

    def shift_end_prep(self, e):
        self.adv.charge_p('shift_end',100)

    def ds_proc(self):
        from core.advbase import Selfbuff
        dmg = self.adv.dmg_make('ds',7.50,'s')
        Selfbuff('ds',0.20,20,'att','buff').on()
        return dmg

class Unreleased_FlameSkillHaste(DragonBase):
    ele = 'flame'
    att = 120
    a = [('sp', 0.35)]