from slot import *

class Gilgamesh(DragonBase):
    ele = 'light'
    att = 124
    a = [('a', 0.5)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 1.60,
        'dx1.startup': 21 / 60.0, # c1 frames
        'dx1.hit': 2,

        'dx2.dmg': 1.76,
        'dx2.startup': 24 / 60.0, # c2 frames
        'dx2.hit': 4,

        'dx3.dmg': 2.22,
        'dx3.startup': 35 / 60.0, # c3 frames
        'dx3.recovery': 83 / 60.0, # recovery
        'dx3.hit': 6,

        'ds.dmg': 5.60,
        'ds.recovery': 100 / 60, # skill frames
        'ds.hit': 1,

        'dodge.startup': 33 / 60, # dodge frames
    }

class PopStar_Siren(DragonBase):
    ele = 'light'
    att = 124
    a = [('a', 0.4)]
    dragonform = {
        'exhilaration': 3.0,
        'skill_use': 2,
        'act': 's s end',

        'dx1.dmg': 0.80,
        'dx1.startup': 17 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 0.96,
        'dx2.startup': 39 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 1.44,
        'dx3.startup': 53 / 60.0, # c3 frames
        'dx3.recovery': 720 / 60.0, # recovery unknown but longer than dodge
        'dx3.hit': 1,

        'ds.recovery': 120 / 60, # skill frames
        'ds.hit': 0,

        'dodge.startup': 41 / 60, # dodge frames
    }

    def ds_proc(self):
        from core.advbase import Teambuff
        Teambuff('d_att_buff',0.20,20).on()
        Teambuff('s1', 0.25, 15, 'defense').on()
        self.adv.energy.add(3, team=True)
        return 0

class Cupid(DragonBase):
    ele = 'light'
    att = 119
    a = [('a', 0.6)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.01,
        'dx1.startup': 17 / 60.0, # c1 frames
        'dx1.hit': 3,

        'dx2.dmg': 2.20,
        'dx2.startup': 38 / 60.0, # c2 frames
        'dx2.hit': 4,

        'dx3.dmg': 2.80,
        'dx3.startup': 53 / 60.0, # c3 frames
        'dx3.recovery': 39 / 60.0, # recovery unknown but longer than dodge
        'dx3.hit': 5,

        'ds.recovery': 140 / 60, # skill frames
        'ds.hit': 0,

        'dodge.startup': 39 / 60, # dodge frames
    }

    def ds_proc(self):
        from core.advbase import Teambuff
        Teambuff('d_cc_buff',0.25,15).on()
        return 0

class Takemikazuchi(DragonBase):
    ele = 'light'
    att = 124
    a = [('od', 0.25), ('a', 0.4)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 1.53,
        'dx1.startup': 20 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 1.68,
        'dx2.startup': 34 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.44,
        'dx3.startup': 44 / 60.0, # c3 frames
        'dx3.recovery': 53 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.dmg': 9.95,
        'ds.recovery': 188 / 60, # skill frames
        'ds.hit': 5,

        'dodge.startup': 39 / 60, # dodge frames
    }

class Corsaint_Phoenix(DragonBase):
    ele = 'light'
    att = 124
    a = [('k_paralysis', 0.2), ('a', 0.5)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.20,
        'dx1.startup': 17 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.53,
        'dx2.startup': 58 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.74,
        'dx3.startup': 30 / 60.0, # c3 frames
        'dx3.recovery': 19 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.dmg': 9.95,
        'ds.recovery': 150 / 60, # skill frames
        'ds.hit': 7,
    }

    def ds_proc(self):
        dmg = self.adv.dmg_make('ds',1.30,'s')
        self.adv.afflics.paralysis('ds',110,0.883,13,dtype='s')
        return dmg + self.adv.dmg_make('ds',1.30*6,'s')

C_Phoenix = Corsaint_Phoenix

class Daikokuten(DragonBase):
    ele = 'light'
    att = 124
    a = [('a', 0.25, 'hit15'), ('a', 0.55)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.55,
        'dx1.startup': 18 / 60.0, # c1 frames
        'dx1.hit': 3,

        'dx2.dmg': 2.92,
        'dx2.startup': 39 / 60.0, # c2 frames
        'dx2.hit': 4,

        'dx3.dmg': 4.10,
        'dx3.startup': 39 / 60.0, # c3 frames
        'dx3.recovery': 66 / 60.0, # recovery
        'dx3.hit': 5,

        'ds.recovery': 120 / 60, # skill frames
        'ds.hit': 1,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from core.advbase import Spdbuff
        self.ds_buff = Spdbuff('ds',0.2,10,wide='team')
        self.ds_buff.bufftime = self.ds_buff._no_bufftime

    def ds_proc(self):
        self.ds_buff.on()
        return self.adv.dmg_make('ds',7.00,'s')

class Tie_Shan_Gongzhu(DragonBase):
    ele = 'light'
    att = 124
    a = [('sp', 0.35)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.30,
        'dx1.startup': 31 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.52,
        'dx2.startup': 36 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.45,
        'dx3.startup': 42 / 60.0, # c3 frames
        'dx3.recovery': 55 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.recovery': 110 / 60, # skill frames
        'ds.hit': 5,
    }
    def ds_proc(self):
        count = self.adv.dmg_make('ds',7.00,'s')
        self.adv.energy.add(5, team=True)
        return count


class Unreleased_LightSkillDamage(DragonBase):
    ele = 'light'
    att = 128
    a = [('s', 0.9), ('a', 0.2)]

class Unreleased_LightCritDamage(DragonBase):
    ele = 'light'
    att = 127
    a = [('a', 0.45), ('cd', 0.55)]

class Unreleased_LightPrimedStr(DragonBase):
    ele = 'light'
    att = 127
    a = [('primed_att', 0.15), ('a', 0.45)]