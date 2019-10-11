from slot import *

class Marishiten(DragonBase):
    ele = 'shadow'
    att = 121

class Shinobi(DragonBase):
    ele = 'shadow'
    att = 128
    aura = [('att','passive',0.2),
            ('s','passive',0.9)]

class Juggernaut(DragonBase):
    ele = 'shadow'
    att = 102
    aura = ('att', 'passive', 0.4)

class Shinobi_0ub(DragonBase):
    ele = 'shadow'
    att = 58
    aura = [('att','passive',0.1),
            ('s','passive',0.7)]

class Nyarlathotep(DragonBase):
    ele = 'shadow'
    att = 128
    aura = ('att','passive',0.50,'hp30')

class Chthonius(DragonBase):
    ele = 'shadow'
    att = 128
    aura = ('att','passive',0.55)

    def oninit(this, adv):
        DragonBase.oninit(this, adv)
        this.adv = adv
        if adv.condition('shapeshift at start and halfway'):
            adv.Buff('dragon_might', 0.15, -1).on()
        else:
            adv.Buff('dragon_might', 0.05, -1).on()
        # adv.Buff('dragon_might', 0.05, -1).on()