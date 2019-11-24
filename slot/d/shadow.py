from slot import *
from math import ceil

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
    aura = ('att', 'passive', 0.45)

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
        this.bloody_tongue(0)
        buff_rate = 15
        if adv.condition('low HP every {}s'.format(buff_rate)):
            from adv.adv_test import sim_duration
            buff_times = ceil(sim_duration/buff_rate)
            for i in range(1, buff_times):
                adv.Timer(this.bloody_tongue).on(buff_rate*i)

    def bloody_tongue(this, t):
        this.adv.Buff('bloody_tongue',0.30, 20).on()

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
            this.dragon_might(0)
        adv.Timer(this.dragon_might).on(timing).on()

    def dragon_might(this, t):
        this.adv.Buff('dragon_might',0.10, -1)

class Unreleased_Shadow35Haste(DragonBase):
    ele = 'shadow'
    att = 120
    aura = [('sp','passive',0.35)]
