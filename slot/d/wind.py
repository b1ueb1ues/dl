from slot import *

class Zephyr(DragonBase):
    ele = 'wind'
    att = 127

class Longlong(DragonBase):
    ele = 'wind'
    att = 127
    aura = [('att','passive',0.45),
            ('crit','damage',0.55)]

class Pazuzu(DragonBase):
    ele = 'wind'
    att = 126
    aura = ('att','passive',0.5)

    def oninit(this, adv):
        DragonBase.oninit(this, adv)
        this.adv = adv
        m = adv.Modifier('pzz','att','killer',0)
        m.get = this.getbane

    def getbane(this):
        return this.adv.afflics.poison.get()*0.2

class Vayu(DragonBase):
    ele = 'wind'
    att = 126
    aura = [('att','passive',0.2),
            ('s','passive',0.9)]

class Vayu_0ub(DragonBase):
    ele = 'wind'
    att = 57
    aura = [('att','passive',0.1),
            ('s','passive',0.7)]

class Roc(DragonBase):
    ele = 'wind'
    att = 101
    aura = ('att', 'passive', 0.45)

class Freyja(DragonBase):
    ele = 'wind'
    att = 120
    aura = [('sp','passive',0.35)]


