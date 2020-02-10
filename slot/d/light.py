from slot import *

class Gilgamesh(DragonBase):
    ele = 'light'
    att = 124
    a = [('a', 0.5)]

class PopStar_Siren(DragonBase):
    ele = 'light'
    att = 124
    a = [('a', 0.4)]
    dragonform = {
        'duration': 13.0, # 13s dragon time
        'act': 's c3 c3 s end',

        'dx1.dmg': 0.80,
        'dx1.startup': 17 / 60.0, # c1 frames
        'dx1.recovery': 39 / 60.0, # c2 frames
        'dx1.hit': 1,

        'dx2.dmg': 0.96,
        'dx2.startup': 0,
        'dx2.recovery': 53 / 60.0, # c3 frames
        'dx2.hit': 1,

        'dx3.dmg': 1.44,
        'dx3.startup': 0,
        'dx3.recovery': 41 / 60.0, # dodge frames, real recovery 53
        'dx3.hit': 1,

        'ds.recovery': 120 / 60, # skill frames
        'ds.hit': 0,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from module.energy import Energy
        self.ds_charges = 2
        Energy(adv, self={}, team={})
        self.energy = self.adv.Event('add_energy')
        self.energy.name = 'team'

    def ds_proc(self):
        self.ds_charges -= 1
        if self.ds_charges > 0:
            self.adv.dragonform.has_skill = True
        from adv import Teambuff, Event
        Teambuff('d_att_buff',0.20,20).on()
        Event('defchain')()
        for _ in range(0, 3):
            self.energy()
        return 0

class Cupid(DragonBase):
    ele = 'light'
    att = 119
    a = [('a', 0.6)]

class Takemikazuchi(DragonBase):
    ele = 'light'
    att = 124
    a = [('od', 0.25), ('a', 0.4)]

class Corsaint_Phoenix(DragonBase):
    ele = 'light'
    att = 124
    a = [('k_paralysis', 0.2), ('a', 0.5)]
C_Phoenix = Corsaint_Phoenix

class Shishimai(DragonBase):
    ele = 'light'
    att = 75
    a = [('cd', 0.7)]

class Daikokuten(DragonBase):
    ele = 'light'
    att = 124
    a = [('a', 0.25, 'hit15'), ('a', 0.55)]
    dragonform = {
        'act': 'c3 c1 s',

        'dx1.dmg': 2.55,
        'dx1.startup': 18 / 60.0, # c1 frames
        'dx1.recovery': 39 / 60.0, # c2 frames
        'dx1.hit': 3,

        'dx2.dmg': 2.92,
        'dx2.startup': 0,
        'dx2.recovery': 39 / 60.0, # c3 frames
        'dx2.hit': 4,

        'dx3.dmg': 4.10,
        'dx3.startup': 0,
        'dx3.recovery': 40 / 60.0, # dodge frames, real recovery 66
        'dx3.hit': 5,

        'ds.recovery': 120 / 60, # skill frames
        'ds.hit': 1,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from adv import Spdbuff
        self.ds_buff = Spdbuff('ds',0.2,10,wide='team')
        self.ds_buff.bufftime = self.ds_buff.nobufftime

    def ds_proc(self):
        self.ds_buff.on()
        return self.adv.dmg_make('d_ds',7.00,'s')

class Unreleased_LightSkillDamage(DragonBase):
    ele = 'light'
    att = 128
    a = [('s', 0.9), ('a', 0.2)]

class Unreleased_LightSkillHaste(DragonBase):
    ele = 'light'
    att = 120
    a = [('sp', 0.35)]

class Unreleased_LightCritDamage(DragonBase):
    ele = 'light'
    att = 127
    a = [('a', 0.45), ('cd', 0.55)]

class Unreleased_LightPrimedStr(DragonBase):
    ele = 'light'
    att = 127
    a = [('primed_att', 0.15), ('a', 0.45)]

class Unreleased_DKR_Dont_hurt_me(DragonBase):
    ele = 'light'
    att = 127
    a = [('a', 0.55), ('fs', 0.60), ('sp',0.30,'fs')]