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

    def oninit(this, adv):
        DragonBase.oninit(this, adv)
        this.adv = adv
        this.bloody_tongue()
        if adv.condition('low HP 3 times'):
            from adv.adv_test import sim_duration
            timing = sim_duration/3
            adv.Timer(this.bloody_tongue).on(timing)
            adv.Timer(this.bloody_tongue).on(timing*2)

    def bloody_tongue(this):
        this.adv.buff('bloody_tongue',0.30, 20)

class Chthonius(DragonBase):
    ele = 'shadow'
    att = 128
    aura = ('att','passive',0.55)

    def oninit(this, adv):
        DragonBase.oninit(this, adv)
        this.adv = adv
        from adv.adv_test import sim_duration
        timing = sim_duration/2
        if adv.condition('shapeshift at start and halfway'):
            this.dragon_might()
        adv.Timer(this.dragon_might).on(timing)
    
    def dragon_might(this):
        this.adv.buff('dragon_might',0.10, -1)