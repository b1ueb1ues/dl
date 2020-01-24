from slot import *
from math import ceil

class Marishiten(DragonBase):
    ele = 'shadow'
    att = 121
    a = [('a', 0.6)]

class Shinobi(DragonBase):
    ele = 'shadow'
    att = 128
    a = [('s', 0.9), ('a', 0.2)]

class Parallel_Zodiark(DragonBase):
    ele = 'shadow'
    att = 77
    a = [('a', 0.2), ('cd', 0.4)]

class Nyarlathotep(DragonBase):
    ele = 'shadow'
    att = 128
    a = [('a', 0.5, 'hp30')]

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
    a = [('a',0.55)]

    def oninit(this, adv):
        DragonBase.oninit(this, adv)
        this.adv = adv
        from adv.adv_test import sim_duration
        timing = int(sim_duration/2)
        def dragon_might(t):
            this.adv.Buff('dragon_might',0.10, -1).on()
        if adv.condition('shapeshift at {}s'.format(timing)):
            adv.Timer(dragon_might).on(timing)

class Unreleased_ShadowSkillHaste(DragonBase):
    ele = 'shadow'
    att = 120
    a = [('sp', 0.35)]

class Unreleased_ShadowPoisonPunish(DragonBase):
    ele = 'shadow'
    att = 127
    a = [('k_poison', 0.2), ('a', 0.5)]