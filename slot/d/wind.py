from slot import *

class Zephyr(DragonBase):
    ele = 'wind'
    att = 127
    a = [('a', 0.6)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.56,
        'dx1.startup': 22 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.82,
        'dx2.startup': 80 / 60.0, # c2 frames
        'dx2.hit': 2,

        'dx3.dmg': 3.58,
        'dx3.startup': 57 / 60.0, # c3 frames
        'dx3.recovery': 60 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.dmg': 8.022,
        'ds.recovery': 177 / 60, # skill frames
        'ds.hit': 3,

        'dodge.startup': 39 / 60, # dodge frames
    }

class Pazuzu(DragonBase):
    ele = 'wind'
    att = 127
    a = [('k_poison', 0.2), ('a', 0.5)]
    dragonform = {
        'act': 'c2 s',

        'dx1.dmg': 1.40,
        'dx1.startup': 20 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 1.54,
        'dx2.startup': 38 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 1.93,
        'dx3.startup': 38 / 60.0, # c3 frames
        'dx3.recovery': 47 / 60.0, # recovery
        'dx3.hit': 3,

        'ds.recovery': 146 / 60, # skill frames
        'ds.hit': 5,

        'dodge.startup': 39 / 60, # dodge frames
    }

    def oninit(self, adv):
        super().oninit(adv)
        from core.advbase import Debuff
        self.ds_buff = Debuff('ds',0.05,10)

    def ds_proc(self):
        dmg = self.adv.dmg_make('ds',0.91,'s')
        self.ds_buff.on()
        self.adv.afflics.poison('ds',120,0.291,30,dtype='s')
        return dmg + self.adv.dmg_make('ds',4*0.91,'s')

class Long_Long(DragonBase):
    ele = 'wind'
    att = 127
    a = [('a', 0.45), ('cd', 0.55)]
    dragonform = {
        'act': 'c3 c5 c5 c3 s c4',

        'dx1.dmg': 1.60,
        'dx1.startup': 11 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 1.68,
        'dx2.startup': 21 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 1.76,
        'dx3.startup': 27 / 60.0, # c3 frames
        'dx3.hit': 1,

        'dx4.dmg': 1.86,
        'dx4.startup': 43 / 60.0, # c4 frames
        'dx4.hit': 2,

        'dx5.dmg': 2.40786,
        'dx5.startup': 28 / 60.0, # c5 frames
        'dx5.recovery': 720 / 60.0, # recovery unknown but longer than dodge
        'dx5.hit': 1,

        'ds.dmg': 5.58,
        'ds.recovery': 166 / 60, # skill frames
        'ds.hit': 5,

        'dodge.startup': 36 / 60, # dodge frames
    }

class Freyja(DragonBase):
    ele = 'wind'
    att = 120
    a = [('sp', 0.35)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 1.60,
        'dx1.startup': 20 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 1.76,
        'dx2.startup': 26 / 60.0, # c2 frames
        'dx2.hit': 2,

        'dx3.dmg': 3.99,
        'dx3.startup': 49 / 60.0, # c3 frames
        'dx3.recovery': 45 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.recovery': 105 / 60, # skill frames
        'ds.hit': -1,

        'dodge.startup': 39 / 60, # dodge frames
    }

    def ds_proc(self):
        self.adv.energy.add(5, team=True)

class Vayu(DragonBase):
    ele = 'wind'
    att = 127
    a = [('s', 0.9), ('a', 0.2)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.08,
        'dx1.startup': (16+19) / 60.0, # c1 frames
        'dx1.hit': 2,

        'dx2.dmg': 2.26,
        'dx2.startup': 34 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.69,
        'dx3.startup': 79 / 60.0, # c3 frames
        'dx3.recovery': 80 / 60.0, # dodge frames, real recovery 80
        'dx3.hit': 1,

        'ds.recovery': 100 / 60, # skill frames
        'ds.hit': 1,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from core.advbase import SingleActionBuff
        self.ds_buff = SingleActionBuff('d_sd_buff',0.40,1,'s','buff')

    def ds_proc(self):
        dmg = self.adv.dmg_make('ds',8.96,'s')
        self.ds_buff.on(1)
        return dmg

class Hastur(DragonBase):
    ele = 'wind'
    att = 127
    a = [('primed_att', 0.15), ('a', 0.45)]
    dragonform = {
        'act': 'c2 s',

        'dx1.dmg': 1.90,
        'dx1.startup': 18 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.28,
        'dx2.startup': 35 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.42,
        'dx3.startup': 49 / 60.0, # c3 frames
        'dx3.recovery': 70 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.dmg': 5.90,
        'ds.recovery': 120 / 60, # skill frames
        'ds.hit': 6,
    }

class AC011_Garland(DragonBase):
    ele = 'wind'
    att = 127
    a = [('a', 0.5)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 1.80,
        'dx1.startup': 18 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.88,
        'dx2.startup': 50 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 2.97,
        'dx3.startup': 39 / 60.0, # c3 frames
        'dx3.recovery': 69 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.dmg': 5.50,
        'ds.recovery': 90 / 60, # skill frames
        'ds.hit': 1,
    }

    def oninit(self, adv):
        DragonBase.oninit(self, adv)
        self.adv = adv
        if adv.condition('maintain shield'):
            adv.Timer(self.dauntless_rampart).on(15)

    def dauntless_rampart(self, t):
        self.adv.Buff('dauntless_rampart',0.30,-1,'att','passive').on()
Garland = AC011_Garland

class Ariel(DragonBase):
    ele = 'wind'
    att = 126
    a = [('a', 0.50), ('sp',0.30)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 1.90,
        'dx1.startup': 19 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.09,
        'dx2.startup': 38 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 0.82,
        'dx3.startup': 60 / 60.0, # c3 frames
        'dx3.recovery': 58 / 60.0, # recovery
        'dx3.hit': 3,

        'ds.dmg': 12.00,
        'ds.recovery': 145 / 60, # skill frames
        'ds.hit': 1,
    }