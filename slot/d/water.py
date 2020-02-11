from slot import *

class Leviathan(DragonBase):
    ele = 'water'
    att = 125
    a = [('a', 0.6)]
    dragonform = {
        'act': 'c2 s',

        'dx1.dmg': 2.92,
        'dx1.startup': 14 / 60.0, # c1 frames
        'dx1.recovery': 47 / 60.0, # c2 frames
        'dx1.hit': 1,

        'dx2.dmg': 4.44,
        'dx2.recovery': 39 / 60.0, # dodge
        'dx2.hit': 2,

        # Levi c3 is a myth

        'ds.recovery': 181 / 60, # skill frames
        'ds.hit': 7,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from core.advbase import Teambuff
        self.ds_buff = Teambuff('ds_bog',0.5,8,1,'att','bog')
        self.ds_buff.bufftime = self.ds_buff.nobufftime

    def ds_proc(self):
        dmg = self.adv.dmg_make('d_ds',9.135,'s')
        r = self.adv.afflics.bog('ds',180)
        if r:
            self.ds_buff.mod_value = 0.5*r
            self.ds_buff.on()
        return dmg

class Siren(DragonBase):
    ele = 'water'
    att = 125
    a = [('s', 0.9), ('a', 0.2)]

class Dragonyule_Jeanne(DragonBase):
    ele = 'water'
    att = 125
    a = [('a', 0.45), ('cc', 0.20)]
DJ = Dragonyule_Jeanne

class Simurgh(DragonBase):
    ele = 'water'
    att = 113
    a = [('od', 0.6)]

class Halloween_Maritimus(DragonBase):
    ele = 'water'
    att = 119
    a = [('sp', 0.35)]
H_Maritimus = Halloween_Maritimus

class Kamuy(DragonBase):
    ele = 'water'
    att = 125
    a = [('primed_att', 0.15), ('a', 0.45)]

class Unreleased_WaterCritDamage(DragonBase):
    ele = 'water'
    att = 127
    a = [('a', 0.45), ('cd', 0.55)]

class Unreleased_Water80Str(DragonBase):
    ele = 'water'
    att = 127
    a = [('a', 0.8, 'some wacky condition')]

class Unreleased_DKR_What_is_love(DragonBase):
    ele = 'water'
    att = 127
    a = [('a', 0.55), ('fs', 0.60), ('sp',0.30,'fs')]