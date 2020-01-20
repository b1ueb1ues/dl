from slot import *

class Cerberus(DragonBase):
    ele = 'flame'
    att = 127

class Sakuya(DragonBase):
    ele = 'flame'
    att = 127
    aura = [('att','passive',0.2),
            ('s','passive',0.9)]

class Arctos(DragonBase):
    ele = 'flame'
    att = 121
    aura = [('att','passive',0.45),
            ('crit','damage',0.55)]

class Apollo(DragonBase):
    ele = 'flame'
    att = 126
    aura = ('att','passive',0.5)

    def oninit(this, adv):
        DragonBase.oninit(this, adv)
        this.adv = adv
        m = adv.Modifier('apl','att','killer',0)
        m.get = this.getbane

    def getbane(this):
        return this.adv.afflics.burn.get()*0.2

class Ifrit(DragonBase):
    ele = 'flame'
    att = 101
    aura = [('att','passive',0.45)]

class Prometheus(DragonBase):
    ele = 'flame'
    att = 121
    aura = [('att','passive',0.50)]

class Unreleased_Flame35Haste(DragonBase):
    ele = 'flame'
    att = 120
    aura = [('sp','passive',0.35)]