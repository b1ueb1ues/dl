from slot import *

class Leviathan(DragonBase):
    ele = 'water'
    att = 125
    a = [('a', 0.6)]
    dragonform = {
        'act': 'c2 s',

        'dx1.dmg': 2.92,
        'dx1.startup': 14 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 4.44,
        'dx2.startup': 47 / 60.0, # c2 frames
        'dx2.recovery': 720 / 60.0, # recovery unknown but longer than dodge
        'dx2.hit': 2,

        # Levi c3 is a myth

        'ds.recovery': 181 / 60, # skill frames
        'ds.hit': 1,

        'dodge.startup': 39 / 60
    }

    def ds_proc(self):
        dmg = self.adv.dmg_make('ds',9.135,'s')
        self.adv.afflics.bog('ds',180)
        return dmg

class Siren(DragonBase):
    ele = 'water'
    att = 125
    a = [('s', 0.9), ('a', 0.2)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.30,
        'dx1.startup': 26 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.53,
        'dx2.startup': 38 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 4.03,
        'dx3.startup': 38 / 60.0, # c3 frames
        'dx3.recovery': 49 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.recovery': 178 / 60, # skill frames
        'ds.hit': -1,

        'dodge.startup': 42 / 60, # dodge frames
    }

    def oninit(self, adv):
        super().oninit(adv)
        from core.advbase import SingleActionBuff
        self.ds_buff = SingleActionBuff('d_sd_buff',0.40,1,'s','buff')

    def ds_proc(self):
        dmg = self.adv.dmg_make('ds',5.00,'s')
        self.ds_buff.on(1)
        return dmg

class Dragonyule_Jeanne(DragonBase):
    ele = 'water'
    att = 125
    a = [('a', 0.45), ('cc', 0.20)]
    dragonform = {
        'act': 'c2 s',

        'dx1.dmg': 1.85,
        'dx1.startup': 17 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.54,
        'dx2.startup': 42 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 2.59,
        'dx3.startup': 39 / 60.0, # c3 frames
        'dx3.recovery': 720 / 60.0, # recovery unknown but longer than dodge
        'dx3.hit': 1,

        'ds.dmg': 6.12,
        'ds.recovery': 164 / 60, # skill frames
        'ds.hit': 3,

        'dodge.startup': 39 / 60, # dodge frames
    }
DJ = Dragonyule_Jeanne

class Simurgh(DragonBase):
    ele = 'water'
    att = 113
    a = [('od', 0.6)]
    dragonform = {
        'act': 'c2 s',

        'dx1.dmg': 1.80,
        'dx1.startup': 22 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 3.42,
        'dx2.startup': 60 / 60.0, # c2 frames
        'dx2.hit': 2,

        'dx3.dmg': 3.78,
        'dx3.startup': 51 / 60.0, # c3 frames
        'dx3.recovery': 49 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.dmg': 6.48,
        'ds.recovery': 132 / 60, # skill frames
        'ds.hit': 12,

        'dodge.startup': 39 / 60, # dodge frames
    }

class Halloween_Maritimus(DragonBase):
    ele = 'water'
    att = 119
    a = [('sp', 0.35)]
    dragonform = {
        'act': 'c3 c3 c3 s',

        'dx1.dmg': 2.00,
        'dx1.startup': 18 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.20,
        'dx2.startup': 40 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 7.60,
        'dx3.startup': 86 / 60.0, # c3 frames
        'dx3.recovery': 46 / 60.0, # recovery
        'dx3.hit': 2,

        'ds.recovery': 151 / 60, # skill frames
        'ds.hit': -1,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from core.advbase import Teambuff
        self.ds_buff = Teambuff('ds_sd',0.3,10,'s','buff')
        self.ds_buff.bufftime = self.ds_buff._no_bufftime

    def ds_proc(self):
        self.ds_buff.on()
        return 0
H_Maritimus = Halloween_Maritimus

class Kamuy(DragonBase):
    ele = 'water'
    att = 125
    a = [('primed_att', 0.15), ('a', 0.45)]

    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 1.90,
        'dx1.startup': 27 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.09,
        'dx2.startup': 41 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 4.18,
        'dx3.startup': 34 / 60.0, # c3 frames
        'dx3.recovery': 73 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.dmg': 0,
        'ds.recovery': 164 / 60, # skill frames
        'ds.hit': 4,
    }

class Nimis(DragonBase):
    ele = 'water'
    att = 125
    a = [('a', 0.45), ('cd', 0.55)]

    dragonform = {
        'act': 'c3 c3 s',

        'dx1.dmg': 2.70,
        'dx1.startup': 5 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.97,
        'dx2.startup': 81 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 5.14,
        'dx3.startup': 64 / 60.0, # c3 frames
        'dx3.recovery': 35 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.dmg': 0,
        'ds.recovery': 146 / 60, # skill frames
        'ds.hit': 0,

        'dodge.startup': 41 / 60, # dodge frames
    }

    def ds_proc(self):
        from core.timeline import now
        self.adv.dragonform.dragon_gauge += 200
        max_time = self.adv.dragonform.dtime() - self.adv.dragonform.conf.dshift.startup
        cur_time = self.adv.dragonform.shift_end_timer.timing - now()
        add_time = min(abs(max_time - cur_time), 5)
        self.adv.dragonform.shift_end_timer.add(add_time)
        return 0

class Gaibhne_and_Creidhne(DragonBase):
    ele = 'water'
    att = 125
    a = [('scharge', 0.35), ('a', 0.45)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.40,
        'dx1.startup': 20 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.64,
        'dx2.startup': 36 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 4.32,
        'dx3.startup': 58 / 60.0, # c3 frames
        'dx3.recovery': 56 / 60.0, # recovery
        'dx3.hit': 2,

        'ds.dmg': 0,
        'ds.recovery': 150 / 60, # skill frames
        'ds.hit': 0,

        'dodge.startup': 40 / 60, # dodge frames
    }

    def ds_proc(self):
        from core.timeline import Timer
        def autocharge(t):
            self.adv.charge_p('ds', 0.091)
        charge = Timer(autocharge, 0.9, True).on()
        def autocharge_off(t):
            charge.off()
        Timer(autocharge_off, 10, True).on()
        return 0

class Unreleased_WaterFrostbitePunish(DragonBase):
    ele = 'water'
    att = 127
    a = [('k_frostbite', 0.2), ('a', 0.5)]

class Unreleased_Water80Str(DragonBase):
    ele = 'water'
    att = 127
    a = [('a', 0.8, 'some wacky condition')]