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
        if this.adv.afflics.get('poison'):
            return 0.2
        else:
            return 0

