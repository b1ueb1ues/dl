from slot import *

class Zephyr(DragonBase):
    ele = 'wind'
    att = 127
    a = [('a', 0.6)]

class Pazuzu(DragonBase):
    ele = 'wind'
    att = 127
    a = [('k_poison', 0.2), ('a', 0.5)]

class Long_Long(DragonBase):
    ele = 'wind'
    att = 127
    a = [('a', 0.45), ('cd', 0.55)]

class Freyja(DragonBase):
    ele = 'wind'
    att = 120
    a = [('sp', 0.35)]

class Vayu(DragonBase):
    ele = 'wind'
    att = 127
    a = [('s', 0.9), ('a', 0.2)]

class Hastur(DragonBase):
    ele = 'wind'
    att = 127
    a = [('primed_att', 0.15), ('a', 0.45)]

class Garland(DragonBase):
    ele = 'wind'
    att = 127
    a = [('a', 0.5)]

    def oninit(this, adv):
        DragonBase.oninit(this, adv)
        this.adv = adv
        if adv.condition('maintain shield'):
            adv.Timer(this.dauntless_rampart).on(15)

    def dauntless_rampart(this, t):
        this.adv.Buff('dauntless_rampart',0.30,-1,'att','passive').on()

class Unreleased_DKR_Baby_dont_hurt_me(DragonBase):
    ele = 'wind'
    att = 127
    a = [('a', 0.55), ('fs', 0.60), ('sp',0.30,'fs')]